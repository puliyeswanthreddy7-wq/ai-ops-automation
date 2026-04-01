from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import pandas as pd

def ask_ai(question):
    df = pd.read_csv("data/sales.csv")
    df["revenue"] = df["sales"] * df["price"]
    df["low_inventory"] = df["inventory"] < 10
    q = question.lower()

    if "highest revenue" in q or "top sku" in q:
        top = df.loc[df["revenue"].idxmax()]
        return f"Top SKU is {top['sku']} with revenue {top['revenue']}"
    if "low inventory" in q:
        low = df[df["low_inventory"]]
        return "Low inventory SKUs: " + ", ".join(low["sku"].tolist()) if not low.empty else "No low inventory items found."
    return "Try asking about highest revenue or low inventory."