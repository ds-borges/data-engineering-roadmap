from database import Base
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func


class ProductModel(Base):
    __tablename__ = "produtcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    supplier_mail = Column(String)
    create_at = Column(DateTime(timezone=True), default=func.now())
