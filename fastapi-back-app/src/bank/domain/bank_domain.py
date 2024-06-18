
from pydantic import BaseModel

from core.domain.core_domain import _CatalogModel


class BankModel(BaseModel, _CatalogModel):
    pass
