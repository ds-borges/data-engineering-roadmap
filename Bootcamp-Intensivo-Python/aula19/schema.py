from typing import Union

from pydantic import BaseModel, PositiveFloat, PositiveInt


class ItemBase(BaseModel):
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None


# Usado para criar um produto sem preocupar com id
class ItemCreate(ItemBase):
    pass


# Usado para consultar um produto a partir do Id
class Item(ItemBase):
    id: PositiveInt
