import uuid

from fastapi import APIRouter

from app.models.user import User, UserCreate

router = APIRouter()

users = []


@router.get("/users")
def get_users(name: str | None = None):
    if name is None:
        return {"users": users}

    filtered_users = []

    for user in users:
        if user["name"] == name:
            filtered_users.append(user)

    return {"users": filtered_users}


@router.post("/users")
def create_user(user: UserCreate):
    new_user = User(id=str(uuid.uuid4()), name=user.name, age=user.age)

    dumped_user = new_user.model_dump()
    users.append(dumped_user)

    return {"message": "User created", "user": dumped_user}


@router.get("/users/{user_id}")
def get_user(user_id: str):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}

    return {"error": "User not found"}
