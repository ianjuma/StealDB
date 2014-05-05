#! /usr/bin/python

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import *

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost/blog', pool_recycle=3600)


users = Table('contact', metadata,
              Column('email', String(50), primary_key=True),
              Column('name', String(50)),
              Column('message', String(50))
              )


class User(Base):
    __tablename__ = 'contact'

    email = Column(String(50), primary_key=True)
    name = Column(String(50))
    message = Column(String(500))
