#!/usr/bin/python3
"""
list the first object from hbtn_0e_6_usa db
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

    # query the database
    first_state = session.query(State).order_by(State.id).first()

    # print the queried database
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
