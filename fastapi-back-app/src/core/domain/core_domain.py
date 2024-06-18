from datetime import datetime

from typing import Annotated, Optional

from pydantic import BeforeValidator, Field, field_validator


PyObjectId = Annotated[str, BeforeValidator(str)]


class _RawModel:
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    created_at: datetime = Field(alias='create_at', default='now')
    update_at: datetime = Field(alias='create_at', default='now')

    @field_validator('created_at', 'update_at', mode='wrap')
    def _set_datetime_now(cls, input_values, handler):
        print('input_values', input_values)
        print('handler', handler)
        return datetime.now()


class _CatalogModel(_RawModel):
    name: str = Field(...)
