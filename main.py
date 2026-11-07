# IN python code 
# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text,"html.parser")

# print(soup.title.text)

# IN FAST API

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://www.dawn.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all("a",class_="story__link"  ):
        title.append(item.text)

    return{
        "news": title[:5]
    }