from models import ProductModel
from schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session


# Função para buscar todos os dados
def get_products(db: Session):
    """
    Função que retorna todos os produtos
    """
    return db.query(ProductModel).all()


# Função para selecionar 1 produto
def get_product(db: Session, product_id: int):
    """
    Função que retorna apenas um produto com base em seu id usando where
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


# Função para inserir
def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Função para atualizar
def update_product(db: Session, product: ProductUpdate, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.supplier_mail is not None:
        db_product.supplier_mail = product.supplier_mail

    db.commit()
    db.refresh(db_product)
    return db_product


# Função para deletar
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
