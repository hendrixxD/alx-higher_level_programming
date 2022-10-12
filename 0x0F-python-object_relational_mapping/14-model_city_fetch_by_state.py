#!/usr/bin/python3
"""
prints all City objects from
the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import State, Base
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in all_states:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
