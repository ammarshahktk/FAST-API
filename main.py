from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message":"Welcome to FastAPI"} 

# About Route
@app.get("/about")
def about():
    return {"message":"This is About Page"} 

# Users Route
@app.get("/users")
def users():
    return {
        "users": ["Ammar", "Waris", "Arbab"]
    } 

