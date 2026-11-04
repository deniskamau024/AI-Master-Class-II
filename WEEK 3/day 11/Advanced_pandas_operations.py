import pandas as pd

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