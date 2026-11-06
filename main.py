from fastapi import FastAPI

app = FastAPI()

#USER ROUTE:
@app.get("/users/{user_id}")
def get_users(user_id:str):
    return {
        "user ID" : user_id
    }

