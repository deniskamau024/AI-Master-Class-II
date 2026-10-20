import requests 
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
if response.status_code == 200:
    user = response.json()

    # Extract specific user information
    name = user["name"]
    username = user["username"]
    email = user["email"]
    city = user["address"]["city"]
    

   # print all the clean data
    print(f"Name:{name}")
    print(f"Username:{username}")
    print(f"Email:{email}")
    print(f"City:{city}")