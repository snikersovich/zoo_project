from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ORM.services.config import DATABASE_URL


Base = declarative_base()
_engine = create_engine(DATABASE_URL, echo=True)
Sessiontocal = sessionmaker(bind=_engine)


def init_db():
    Base.metadat.create_all(bind=_engine)
