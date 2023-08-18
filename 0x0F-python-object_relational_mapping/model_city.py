#!/usr/bin/python3

"""contains the class City and an instance Base imported from model_base
"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_base import Base


class City(Base):
    """
    A class that sets id,name of the table(cities) and states id (based on a
    foreign key from State table)
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
