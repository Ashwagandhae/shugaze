import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("./data/dataset.csv")


def get_days_before_today(date_str) -> float:
    date_obj = None
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%y %I:%M %p")
    except:
        date_obj = datetime.today()

    today = datetime(2025, 2, 22, 15, 0)

    delta = today - date_obj
    return delta.total_seconds() / 60 / 60 / 24


df["time"] = df["time"].map(get_days_before_today)
df = df[(df["time"] > 0) & (df["time"] < 4)]
df.sort_values(by="time", ascending=False, inplace=True)

sneaker_name = "Nike Dunk Low"
unique_names = df["name"].unique()

X = []
y = []

for name in unique_names:
    sneaker_data = df[df["name"] == name].sort_values(by="time", ascending=False)
    prices = sneaker_data["price"].head(10).tolist()
    prices = prices + [0] * (10 - len(prices))
    X.append(prices[:-1])
    y.append(prices[-1])

X = np.array(X)
y = np.array(y)

threshold = 0.8

zero_counts = np.sum(X == 0, axis=1)
zero_percentages = zero_counts / X.shape[1]
valid_rows = zero_percentages < threshold

X_filtered = X[valid_rows]
y_filtered = y[valid_rows]

X_train, X_test, y_train, y_test = train_test_split(
    X_filtered, y_filtered, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


def predict(X):
    return model.predict(X)
