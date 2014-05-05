#! /usr/bin/python

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost/blog', pool_recycle=3600)

class User(Base):
	__tablename__ = 'contact'

	email = Column(String(50), primary_key=True)
	name = Column(String(50))
	message = Column(String(500))