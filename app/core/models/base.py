from sqlalchemy.orm.decl_api import DeclarativeBase


class CoreBase(DeclarativeBase):
    __abstract__: bool = True
