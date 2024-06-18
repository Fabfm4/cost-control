

from fastapi import APIRouter

router = APIRouter(
    prefix="/bank",
    tags=["bank"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_description="Bank API")
async def list_bank():
    return {'hola': 'hola'}
