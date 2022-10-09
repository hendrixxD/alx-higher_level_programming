#!/usr/bin/python3
"""
list all objects using alchemy from hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:\
            {argv[2]}@localhost:3306/{argv[3]}", pool_pre_ping=True)

    # Initilize engine
    Base.metadata.create_all(engine)

    # Create and initialize session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #query the database
    all_states = session.query(State).order_by(State.id).all()

    # print the queried database
    for state in all_states:
        print(f"{state.id}: {state.name}")
