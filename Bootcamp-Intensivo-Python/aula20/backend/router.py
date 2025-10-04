from typing import List

from controller import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product,
)
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import ProductCreate, ProductResponse, ProductUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/products", response_model=List[ProductResponse])
def read_all_products_router(db: Session = Depends(get_db)):
    """
    Essa é minha rota de ler todos os produtos do banco de dados
    """
    products = get_products(db)
    return products


@router.get("/product/{product_id}", response_model=ProductResponse)
def read_one_product_router(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail="Você está querendo buscar um produto que não existe",
        )
    return db_product


@router.post("/products", response_model=ProductResponse)
def create_product_router(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@router.put("/product/{product_id}", response_model=ProductResponse)
def update_product_router(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    product_db = update_product(db=db, product_id=product_id, product=product)

    if product_db is None:
        raise HTTPException(
            status_code=404,
            detail="Você quer fazer um update de um produto que não existe",
        )

    db.commit()
    return product_db


@router.delete("/product/{product_id}", response_model=ProductResponse)
def delete_product_router(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(db=db, product_id=product_id)

    if product_db is None:
        raise HTTPException(
            status_code=404, detail="Você quer deletar um produto que não existe"
        )

    return product_db
