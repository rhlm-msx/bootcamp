'''

Objective of the script is.
- Init Database as per the db.md
    - Create Tables if not created.
    - Add Data with seed files and data.

'''
from typing import Optional
import enum
from enum import auto
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine, text, schema, select, Enum
from sqlalchemy import Table, Column, String, MetaData, Integer,  Identity, Text, UniqueConstraint


class ModTypes(enum.Enum):
    MAIN = auto()
    APP = auto()



def createSchema(name):
    with engine.connect() as conn:
        sql = schema.CreateSchema(name, True).compile(engine).string
        conn.exec_driver_sql(sql)
        conn.commit()



class Base(DeclarativeBase):
    schema = "main"
    pass

class Modules(Base):
    __tablename__ = "modules"
    __table_args__= {"schema": "main"}
    id: Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(Enum(ModTypes, schema="main"), default=ModTypes.APP)
    name: Mapped[str] = mapped_column(String, unique=True)
    route: Mapped[str] = mapped_column(String, unique=True)
    desc: Mapped[str] = mapped_column(Text)
    icon: Mapped[str] = mapped_column(String)

engine = create_engine("postgresql+psycopg2://mind:mind@localhost/mainApp", echo=True)
createSchema("main")

Base.metadata.create_all(engine)

