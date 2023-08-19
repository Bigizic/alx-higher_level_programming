#!/usr/bin/python3
"""
Module containing the City class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class definition of a City
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
