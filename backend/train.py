import pandas as pd
from datetime import datetime
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


df = pd.read_csv("./data/dataset.csv")


def get_days_before_today(date_str) -> float:
    date_obj = datetime.strptime(date_str, "%m/%d/%y %I:%M %p")

    today = datetime(2025, 2, 22, 15, 0)

    delta = today - date_obj
    return delta.total_seconds() / 60 / 60 / 24


def get_points_for_name(name: str) -> list[list[float]]:
    items = df.loc[df["name"] == name]
    items = items.sort_values(by="time", ascending=True)

    ret = []
    for _, row in items.iterrows():
        days_before_today = get_days_before_today(row["time"])
        if days_before_today < 0 or days_before_today > 4:
            continue
        ret.append([days_before_today, float(row["price"])])

    ret.sort(key=lambda x: x[0])
    return ret


unique_names = df["name"].unique().tolist()
print(unique_names)

x = []
y = []

count = 10

for name in unique_names:
    points = get_points_for_name(name)
    for i in range(0, len(points) - count):
        arr = points[i : i + count]
        [_, out] = arr[count - 1]
        x_in = []

        for [t, p] in arr[0 : count - 1]:
            # x_in.append(t)
            x_in.append(p)
        x.append(x_in)
        y.append(out)

x = np.array(x)
y = np.array(y)

# print(x, y)
# print(x.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


model = RandomForestRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")
