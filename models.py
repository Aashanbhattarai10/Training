from sqlalchemy import Column,MetaData,Integer
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

base=declarative_base()
metadata=MetaData()

class UserTBL(base):
    __tablename__='aashan'
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column('first name',NullType)
    last_name=Column('last name',NullType)
    dob=Column('dob',NullType)