from fastapi import APIRouter

from app.models.user import User

router = APIRouter()

users = []


@router.get("/users")
def get_users(name: str = None):
    if name is None:
        return {"users": users}

    filtered_users = []

    for user in users:
        if user["name"] == name:
            filtered_users.append(user)
    return {"users": filtered_users}


@router.post("/users")
def create_user(user: User):
    dumped_user = user.model_dump()
    users.append(dumped_user)
    return {"message": "User created", "user": dumped_user}
