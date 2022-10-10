#!/usr/bin/python3
"""
A script that adds a state object
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':

    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # initialize database
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Adding a new record
    """
    # add an object to State
    state1 = State(name="Lousiana")
    # add new state
    session.add(state1)
    # commit new changes
    session.commit()

    print(state1.id)
    """
    new_state_id = session.query(State).order_by(State.id.desc()).first()
    print(f"{new_state_id.id}")
    """
