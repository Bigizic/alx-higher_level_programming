#!/usr/bin/python3

"""contains the class State and an instance Base of declarative_base()
"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

my_meta_data = MetaData()
Base = declarative_base(metadata=my_meta_data)


class State(Base):
    """
    A class that sets id and name of the table(states)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
