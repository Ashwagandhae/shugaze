from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import AnalyzeRequest, Shoe, AnalyzeResponse, ShoeWithPoints, SearchRequest
import random
import pandas as pd
from gpt import get_similar_shoes_test, get_similar_shoes
from datetime import datetime
from train_2 import predict
import numpy as np
import asyncio


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4242",
]

df = pd.read_csv("./data/dataset.csv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def row_to_shoe(row) -> Shoe:
    return Shoe(
        name=str(row["name"]),
        size=float(row["size"]),
        price=float(row["price"]),
        id=str(row["id"]),
    )


@app.get("/trending/")
async def trending() -> list[Shoe]:
    df_unique = df.drop_duplicates(subset="name")

    items = df_unique.sort_values(by="price", ascending=False).head(100)

    ret = []
    for index, row in items.iterrows():
        ret.append(row_to_shoe(row))
    return ret


@app.post("/search/")
async def search(data: SearchRequest) -> list[Shoe]:
    search_term = data.search

    df_uq = df.drop_duplicates(subset="name")

    filtered_df = df_uq[
        df_uq["name"].str.lower().str.contains(search_term.lower(), na=False)
    ]

    items = filtered_df.head(100)

    ret = []
    for index, row in items.iterrows():
        ret.append(ret.append(row_to_shoe))
    return ret


def random_points() -> list[list[float]]:
    ret: list[list[float]] = []
    for i in range(0, 10):
        ret.append([i / 10, random.randint(0, 200)])
    return ret


@app.post("/analyze/")
async def analyze(data: AnalyzeRequest) -> AnalyzeResponse:
    print("id", data.id)
    row = df.loc[df["id"] == int(data.id)].iloc[0]

    original_shoe = row_to_shoe(row)

    def get_shoes():
        return get_similar_shoes(original_shoe.name)

    similar_names = await asyncio.to_thread(get_shoes)

    print(similar_names)

    similar_names = [name for name in similar_names if name in df["name"].values]

    original = ShoeWithPoints(
        shoe=original_shoe, points=get_points_for_name(original_shoe.name)
    )
    similar = list(
        map(
            lambda name: ShoeWithPoints(
                shoe=get_shoe_for_name(name), points=get_points_for_name(name)
            ),
            similar_names,
        )
    )

    return AnalyzeResponse(
        original=original,
        similar=similar,
        today=0.0,
    )


def get_days_before_today(date_str) -> float:
    date_obj = datetime.strptime(date_str, "%m/%d/%y %I:%M %p")

    today = datetime(2025, 2, 22, 15, 0)

    delta = today - date_obj
    return delta.total_seconds() / 60 / 60 / 24


def get_points_for_name(name: str) -> list[list[float]]:
    items = df.loc[df["name"] == name]
    items = items.sort_values(by="time", ascending=True)

    ret: list[list[float]] = []
    for _, row in items.iterrows():
        days_before_today = get_days_before_today(row["time"])
        if days_before_today < 0 or days_before_today > 4:
            continue
        ret.append([-days_before_today, float(row["price"])])

    ret.sort(key=lambda x: x[0])

    ret = append_predict_futures(ret)

    return ret


def append_predict_futures(ret: list[list[float]]) -> list[list[float]]:
    ret_price = list(map(lambda x: x[1], ret))
    lst = None
    if len(ret_price) < 9:
        lst = [0.0] * (9 - len(ret_price)) + ret_price
    else:
        lst = ret_price[-9:]

    for i in range(1, 4):
        pred = predict(np.array([lst]))[0]
        ret.append([0.25 * i, pred])
        lst.pop(0)
        lst.append(pred)
    return ret


def get_shoe_for_name(name: str) -> Shoe:
    row = df.loc[df["name"] == name].iloc[0]
    return row_to_shoe(row)
