import pandas as pd
import matplotlib.pyplot as plt


# Step 1. Set up a time series dataframe

# Monthly M-Pesa transaction data for Hassan Traders
data = {
    "date": ["2024-01", "2024-02", "2024-03", "2024-04",
              "2024-05", "2024-06", "2024-07", "2024-08"],
    "revenue_kes": [145000, 162000, 158000, 189000,
                    201000, 195000, 218000, 234000]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
print(df)

# step 2. Calculate month over month growth and rolling averages

# Month over month percentage changes
df["growth_pct"] = df["revenue_kes"].pct_change() * 100

# 3-month rolling averages
df["rolling_3m"] = df["revenue_kes"].rolling(3).mean()

print(df[["revenue_kes","growth_pct","rolling_3m"]])

# Step 3
# RESAMPLING DATA TO DIFFERENT FREQUENCY
# Create daily sales data
daily_sales = pd.Series(
    data=[4500, 6200, 3800, 7100, 5500, 8200, 6700],
    index=pd.date_range(start="2024-11-01", periods=7, freq="D")
)

print()
print("=" * 54)
# Sum to weekly
weekly = daily_sales.resample("W").sum()
print("Weekly totals:", weekly)

print()
print("=" * 54)
# Step 4
# plot your time series to spot trends visually
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df.index, df["revenue_kes"], marker="o", label="Monthly Revenue", color="#1F4E79")
ax.plot(df.index, df["rolling_3m"], linestyle="--", label="3-Month Average", color="#2E75B6")

ax.set_title("Hassan Traders: Revenue Jan-Aug 2024")
ax.set_ylabel("Revenue (KES)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("revenue_trend.png", dpi=150)
print("Chart saved: revenue_trend.png")


print()
print("=" * 54)
# step 5
# identify peaks,dips,and outliers in your time series.
# Find the best and worst month
best_month = df["revenue_kes"].idxmax()
worst_month = df["revenue_kes"].idxmin()

print(f"Best month: {best_month.strftime('%B %Y')}, KES {df.loc[best_month, 'revenue_kes']:,}")
print(f"Worst month: {worst_month.strftime('%B %Y')}, KES {df.loc[worst_month, 'revenue_kes']:,}")
print(f"Total 8-month revenue: KES {df['revenue_kes'].sum():,}")
print(f"Overall growth (Jan-Aug): {((df['revenue_kes'].iloc[-1] / df['revenue_kes'].iloc[0]) - 1) * 100:.1f}%")