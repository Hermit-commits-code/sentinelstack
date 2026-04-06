from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
def read_root():
    return {"message": "SentinelStack backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return {"message": "User created", "user": user}
