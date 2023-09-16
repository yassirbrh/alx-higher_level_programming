#!/usr/bin/python3
'''
    Script that lists all City objects from the database hbtn_0e_101_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(usr, pwd, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
