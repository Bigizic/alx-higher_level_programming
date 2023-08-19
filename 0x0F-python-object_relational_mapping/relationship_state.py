#!/usr/bin/python3
"""
Module containing improvement to the State class
"""

from sqlalchemy import Column, Integer, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

my_meta_data = MetaData()
Base = declarative_base(metadata=my_meta_data)


class State(Base):
    """
    Class definition of a State class inheriting from Base()
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
