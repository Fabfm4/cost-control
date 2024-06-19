from fastapi import APIRouter, Body, status

from src.core.domain.core_domain import T, get_collection_model
from src.bank.domain.bank_domain import BankModel


router = APIRouter(
    prefix="/banks",
    tags=["banks"],
    responses={404: {"description": "Not found"}},
)


CollectionModel: type[T] = get_collection_model(BankModel)


@router.get(
        "/",
        response_description="List all banks",
        response_model=CollectionModel,
        response_model_by_alias=False,
        )
async def list_banks():
    return CollectionModel(data=[BankModel(name="Bank of Mexico")])


@router.post(
        "/",
        response_description="Create a new bank",
        response_model=BankModel,
        response_model_by_alias=False,
        status_code=status.HTTP_201_CREATED,
        )
async def create_bank(bank: BankModel = Body(...)):
    print(bank.model_dump(by_alias=True, exclude=["-id"]))
    return bank


@router.get(
        "/{bank_id}",
        response_description="Get a single bank",
        response_model=BankModel,
        response_model_by_alias=False,
        )
async def get_bank(bank_id: str):
    print(bank_id)
    return BankModel(name="Bank of Mexico")


@router.put(
        "/{bank_id}",
        response_description="Update a bank",
        response_model=BankModel,
        response_model_by_alias=False,
        )
async def update_bank(bank_id: str, bank: BankModel = Body(...)):
    print(bank_id)
    print(bank.model_dump(by_alias=True, exclude=["-id"]))
    return bank
