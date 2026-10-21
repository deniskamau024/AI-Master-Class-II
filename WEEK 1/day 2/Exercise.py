import requests
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWSAPI_API_KEY")
url = "https://newsapi.org/v2/everything"

parameters = {
    "q": "technology",  # my search keyword
    "language":"en",    #language filter
    "pagesize":16,   #Number of articles to return
    "apikey":api_key # uses loaded api key from my .env
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    news_data = response.json()
    articles = news_data.get("articles",[])

    print(f"-----Fetched {len("articles")} Atricles Successfully")

    for index,article in enumerate(articles,1):
        title = article.get("title","No Title")
        source = article.get("source",{}.get("name","unknown"))
        url = article.get("url","#")

        print(f"{index}. {title}")
        print(f" Source: {source} | Link: {url}\n")

else:
    print(f"Error {response.status_code}: {response.text}")


