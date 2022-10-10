#!/usr/bin/python3
"""
list all states with an 'a' from hbtn_0e_6_usa db
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Initilize engine
    Base.metadata.create_all(engine)

    # Create and initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all name of states in database
    all_states = session.query(State).all()
    states_list = []
    for state in all_states:
        state_list.append(state.name)

    # query the database to extract the first argument
    s = session.query(State).filter(State.name == argv[4]).first()

    # print the queried database
    if argv[4] not in state_list:
        print("Not found")
    else:
        print(s.id)

    # close session
    session.close()
