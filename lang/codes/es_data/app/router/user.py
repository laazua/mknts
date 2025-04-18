from fastapi import APIRouter


api = APIRouter()


@api.post("/sign")
async def login():
    pass