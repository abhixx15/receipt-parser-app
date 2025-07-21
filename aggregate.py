from statistics import mean, median, mode, StatisticsError
from collections import Counter
import pandas as pd

def compute_stats(data):
    amounts = [float(row[3]) for row in data if isinstance(row[3], (int, float, str)) and str(row[3]).replace('.', '', 1).isdigit()]
    stats = {
        "sum": sum(amounts) if amounts else 0,
        "mean": mean(amounts) if amounts else 0,
        "median": median(amounts) if amounts else 0,
        "mode": None
    }
    try:
        stats["mode"] = mode(amounts) if len(set(amounts)) > 1 else "No unique mode"
    except StatisticsError:
        stats["mode"] = "No mode"
    return stats

def vendor_frequency(data):
    vendors = [row[1] for row in data]
    return Counter(vendors)

def monthly_spend(data):
    df = pd.DataFrame(data, columns=["ID", "Vendor", "Date", "Amount", "Category"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Date", "Amount"])
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Amount"].sum()
