from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="User Service",
    version="1.0.0"
)

# -----------------------------------------
# User Model
# -----------------------------------------

class User(BaseModel):

    username: str

    email: str

    password: str

# -----------------------------------------
# Temporary In-Memory Storage
# -----------------------------------------

users = []

# -----------------------------------------
# Health Endpoint
# -----------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "User Service Healthy"
    }

# -----------------------------------------
# Register User
# -----------------------------------------

@app.post("/register")
def register_user(user: User):

    users.append(user.dict())

    return {
        "message": "User registered successfully",
        "user": user
    }

# -----------------------------------------
# Get All Users
# -----------------------------------------

@app.get("/users")
def get_users():

    return users