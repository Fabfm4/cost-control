from pydantic import BaseModel, ConfigDict

from src.core.domain.core_domain import _CatalogModel


class BankModel(BaseModel, _CatalogModel):

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Bank of Mexico",
                "created_at": "2021-08-01T00:00:00",
                "update_at": "2021-08-01T00:00:00",
            },
        }
    )
