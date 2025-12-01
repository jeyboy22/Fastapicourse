from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users_db = {}

class Register(BaseModel):
    username: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class UserInfo(BaseModel):
    username: str

@app.post("/register")
def register(user: Register):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    users_db[user.username] = user.password
    return {"message": "User registered successfully!"}

@app.post("/login")
def login(user: Login):
    if user.username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "Login successful"}

@app.get("/user/{username}")
def get_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User does not exist")

    return {"username": username, "status": "Active"}
