import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
password = os.getenv("senha_postgres_supabase")

POSTGRESS_DATABASE_URL = (
    f"postgresql://postgres.whashwetuxwqjhjpcaba:{password}"
    "@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
)

engine = create_engine(POSTGRESS_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
