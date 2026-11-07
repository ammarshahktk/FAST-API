# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# data = response.json()
# print(data[:2])


from fastapi import FastAPI,HTTPException
import requests

app = FastAPI()

#GET ALL DATA

@app.get("/post")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

#GET SINGLE DATA
@app.get("/post/{post_id}")
def get_post(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Page Not Found Contact Arbab"
        )
    return response.json()