import pandas as pd

# Merge two DataFrames

orders = pd.DataFrame(
    {"order_id":[101,102,103],
    "customer_id": [1,2,1],
     "amount_kes": [45000,28000,62000] })

customers = pd.DataFrame({
    "customer_id": [1,2,3],
    "name": ["Kamau Stores","Otieno Wholesale","Hassan Traders"],
    "county": ["Nairobi","Kisumu","Mombasa"] })

# Inner join: Only customers who have ordered
merged = pd.merge(orders, customers, on="customer_id", how="inner")
print(merged)

#understanding join types and creating  a pivot-table

sales = pd.DataFrame({
    "month": ["Jan","Jan","Feb","Feb","Mar","Mar"],
    "county":["Nairobi","Kisumu","Nairobi","Kisumu","Nairobi","Kisumu"],
    "revenue_kes": [145000, 89000, 162000, 95000, 178000, 112000]
})
print("=" * 54)
pivot = pd.pivot_table(
    sales,
    values="revenue_kes",
    index="county",
    columns="month",
    aggfunc="sum"
)
print("\n",pivot)

print("=" * 54)

# Using apply to run a custom function on every row.

def classify_sale(amount):
    if amount >= 100000:
        return "Large"
    elif amount >= 50000:
        return "Medium"
    else:
        return "Small"
    
merged["sale_size"] = merged["amount_kes"].apply(classify_sale)
print(merged[["name","amount_kes","sale_size"]])

# Using groupby() with multiple aggregation functions at once

summary =merged.groupby("county").agg(
    total_revenue = ("amount_kes","sum"),
    order_count= ("order_id","count"),
    avg_order = ("amount_kes","mean"),
    largest_order = ("amount_kes","max")
    )
print ("-" * 54)
print(summary)