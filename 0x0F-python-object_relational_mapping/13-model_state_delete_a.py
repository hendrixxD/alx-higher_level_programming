#!/usr/bin/python3
"""
A script that updates state where id = 2
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
    # Delete all states with 'a' in spelling
    session.query(State).filter(State.name.ilike('%a%')).delete()
    """
    # Deleting object instance returned by a query
    # (will issue 2 statements: first SELECT, then DELETE):

    obj = session.query(State).filter(State.name.ilike('%a%')).all()

    for delete in obj:
        session.delete(delete)

    # commit new update
    session.commit()

    """
    # Query new db with new update
    updated_id_2 = session.query(State).all()
    for updated in update_id_2:
        print(f"{update_id_2.id}: {update_id_2.name}")
    """

    session.close()
