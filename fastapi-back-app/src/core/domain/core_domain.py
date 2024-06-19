from datetime import datetime

from typing import Annotated, Optional, Type, TypeVar

from pydantic import BaseModel, BeforeValidator, Field, field_validator


PyObjectId = Annotated[str, BeforeValidator(str)]
T = TypeVar('T', bound=BaseModel)


class _RawModel:
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    created_at: Optional[datetime] = Field(
        alias='create_at', default_factory=datetime.now)
    update_at: datetime = Field(alias='create_at', default=None)

    @field_validator('update_at', mode='wrap')
    def created_at_now(cls, v, handler):
        if v == 'now':
            return datetime.now()
        return handler(v)


class _CatalogModel(_RawModel):
    name: str = Field(...)


def get_collection_model(base_model: type[T]) -> Type[T]:

    class CollectionModel(BaseModel):
        data: Optional[list[base_model]]
        current_page: int = Field(default=0)

    return CollectionModel
