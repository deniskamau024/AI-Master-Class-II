import requests
country_code = "KEN"
url = f"https://api.worldbank.org/v2/country/{country_code}?format=json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    country = data[1][0]

print("Status code:",response.status_code)
print("Country:",country["name"])
print("Region:",country["region"]["value"])
print("Income Level:",country["incomeLevel"]["value"])
print("Data Received:",country)