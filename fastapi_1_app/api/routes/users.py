from fastapi import APIRouter

router = APIRouter(
    tags = ["User Routes"]
)


@router.get("/")
def read_root():
    return {"mgs": "Hellow world"}   