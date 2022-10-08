#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

#creating an instance of create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

#an instance of declarative base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User (name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

#Creating an instance of a mapped class
#int_user = User(name='joshua', fullname='Lenge Joshua', nickname='HendrixxSdiddy')
#print(int_user.name)
#print(int_user.fullname)
#print(str(int_user.id))

"""
#Schema
User.__table__
Table('users', MetaData(bind=None),
        Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
        Column('name', String(), table=<users>),
        Column('fullname', String(), table=<users>),
        Column('nickname', String(), table=<users>, schema=None)
"""

#Creatin a session
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)

#for any conversation with the database, Session is instantiated
session = Session()

#Adding and Updating objects
int_user1 = User(name='lenge', fullname='lege danladi', nickname='Hendrixx')
session.add(int_user1)

our_user = session.query(User).filter_by(name='lenge').first()

#print(our_user)
#print(int_user = our_user)

#Adding  more User objects using add_all()
session.add_all([
    User(name='Dan', fullname='Lenge Josh', nickname='Hendrixx'),
    User(name='Regan', fullname='regan', nickname='twista'),
    User(name='Josh', fullname='Josh lenge', nickname='Kim'),])

#Check for modification if made to any object of User
#print(session.dirty)

#Check for new added Updates
#print(session.new)

#Commit all pending transactions to the database
session.commit()

