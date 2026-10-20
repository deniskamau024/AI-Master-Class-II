import requests
url = "https://restcountries.com/v5/name/kenya"
response =requests.get(url)

print("status code:",response.status_code)
print("Data received",response.json())