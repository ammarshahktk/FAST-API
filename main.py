from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed Origin Frontend URL
origins = [
    "http://127.0.0.1:5500/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allowed Front end
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message" : "CORS ENABLE API"
    }