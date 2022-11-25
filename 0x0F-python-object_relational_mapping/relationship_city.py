#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""

from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer, ForeignKey

Base = declarative_base()
"""
city class inherits from Base clas
"""


class City(Base):

    __tablename__ = 'cities'
    """
    Args:
        id:auto-generated, unique integer
           can’t be null and is a primary key
        name:a string of 128 characters and can’t be null
        state_id: an integer, an integer, cant be null, a foreing key
    """
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
