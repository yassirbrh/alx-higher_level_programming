#!/usr/bin/python3
'''
    Script that lists all State objects from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

usr = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(usr, pwd, db),
    pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
