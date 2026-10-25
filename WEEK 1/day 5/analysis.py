import pandas as pd
import csv

# Read data from csv

df = pd.read_csv("sales.csv")

# Calculate total sales amount

total_sales = df["Amount"].sum()

# Find the sales person with the highest sales
# idmax() locates the row index where the  'Amount' column hits Max value

top_sales_person_row = df.loc[df["Amount"].idxmax()]
top_name = top_sales_person_row["Name"]
top_amount = top_sales_person_row["Amount"]
top_county = top_sales_person_row["County"]

# Print structured results

print("=" * 45)
print(f"SALES SUMMARY REPORT")
print("=" * 45)
print(f"Total Portifolo Revenue: Ksh {total_sales:,}")
print("=" * 45)
print(f"Top performing agent: {top_name}")
print(f"Top agents sales volume: {top_amount:,}")
print(f"Territory Location: {top_county}")
print("=" * 45)