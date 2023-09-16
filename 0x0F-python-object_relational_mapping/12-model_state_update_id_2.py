#!/usr/bin/python3
'''
    Script that lists all State objects from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(usr, pwd, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(query)
    session.commit()
    session.close()
