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

    # query the database
    a_in_state = session.query(State).filter(State.name.ilike('%a%')).\
            order_by(State.id).all()

    # print the queried database
    for _a in a_in_state:
        print("{}: {}".format(_a.id, _a.name))

    session.close()
