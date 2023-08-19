#!/usr/bin/python3

"""contains the class City and an instance Base imported from model_state
"""

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    A class that sets id,name of the table(cities) and states id (based on a
    foreign key from State table)
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

    state = relationship("State")
