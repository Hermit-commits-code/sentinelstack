from fastapi import FastAPI

from app.routes.users import router as users_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "SentinelStack backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(users_router)
