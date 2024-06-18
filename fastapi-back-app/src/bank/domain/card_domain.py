from pydantic import BaseModel, Field

from bank.domain.bank_domain import BankModel
from core.domain.core_domain import _CatalogModel


class CardModel(BaseModel, _CatalogModel):
    bank = BankModel
    last_digits: str = Field(...)
