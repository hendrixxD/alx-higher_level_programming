#!/usr/bin/python3
"""first state model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
engine = create_engine('mysql+mysqldb://root:
root@localhost:3306/hbtn_0e_6_usa')
"""


class State(Base):
    """table to be created in hbtn_0e_6_usa database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    # relationship with cities
    cities = relationship("City", backref="state", cascade="all, delete")
