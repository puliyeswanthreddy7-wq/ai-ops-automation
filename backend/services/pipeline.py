import pandas as pd

def run_pipeline():
    df = pd.read_csv("data/sales.csv")
    df["revenue"] = df["sales"] * df["price"]
    df["low_inventory"] = df["inventory"] < 10
    return df.to_dict()