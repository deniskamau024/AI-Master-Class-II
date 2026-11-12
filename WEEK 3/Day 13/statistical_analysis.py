import pandas as pd
import numpy as np
from scipy import stats
sales = pd.DataFrame({
    "amount_kes": [12000,45000,8500,67000,23000,890000,15000,34000,11000,52000]
})
print(sales.describe())

print()
print("="*54)
# Selecting and finding outliers
Q1 = sales["amount_kes"].quantile(0.25)
Q3 = sales["amount_kes"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = sales[(sales["amount_kes"] < lower) | (sales["amount_kes"] > upper)]
print(f"Outliers found: {len(outliers)}")
print(outliers)

print()
print("="*54)

# Calculating the correration between amount_kes and ad_spending.
monthly = pd.DataFrame({
    "ad_spend_kes": [5000, 8000, 12000, 15000, 20000, 25000],
    "sales_kes":    [42000, 58000, 74000, 88000, 115000, 142000]
})

corr = monthly["ad_spend_kes"].corr(monthly["sales_kes"])
print(f"Correlation: {corr:.3f}") 

# Corr = 0.999. This means ad spend and sales move almost perfectly together. 
#For every amount spent on advertising sales increase too.

print()
print("="*54)
# Testing whether two groups are actually different.

nairobi_sales = [145000, 162000, 178000, 189000, 201000]
kisumu_sales =  [89000,  95000,  112000, 108000, 121000]

t_stat, p_value = stats.ttest_ind(nairobi_sales, kisumu_sales)
print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference could be due to chance.")