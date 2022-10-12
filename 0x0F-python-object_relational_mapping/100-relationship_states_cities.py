#!/usr/bin/python3
"""
 a script that creates the State “California”
 with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative
from sqlalchemy import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Table
from sys import argv
from relationship_city import City

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                        format(argv[1], argv[2], argv[3]))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session(engine)

state = State(name='California')
city = City(name='San Francisco')

session.commit()
