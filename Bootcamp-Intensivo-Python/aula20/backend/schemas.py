from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveFloat


class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    supplier_mail: EmailStr


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None  # Pode passar ou não os dados
    description: Optional[str] = None  # Pode passar ou não os dados
    price: Optional[PositiveFloat] = None  # Pode passar ou não os dados
    category: Optional[str] = None  # Pode passar ou não os dados
    supplier_mail: Optional[EmailStr] = None  # Pode passar ou não os dados
