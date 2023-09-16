#!/usr/bin/python3
'''
    Script that prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(usr, pwd, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State, City).join(City)
    rows = query.filter(State.id == City.state_id).order_by(City.id).all()
    for row in rows:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
