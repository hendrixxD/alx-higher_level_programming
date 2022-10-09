#!/usr/bin/python3
"""first state model"""

#from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

#engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

class State(Base):
    """table to be created in hbtn_0e_6_usa database
    """
    __table_name__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, None=False, autoincreament=True)
    name = Column(String(128), None=False)
