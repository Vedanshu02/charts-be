from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase
from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, BigInteger, String

Base = declarative_base()


class BaseModel(Base, AbstractConcreteBase):
    __abstrace__ = True

    @declared_attr  # type: ignore
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(BigInteger, primary_key=True, index=True)
   
