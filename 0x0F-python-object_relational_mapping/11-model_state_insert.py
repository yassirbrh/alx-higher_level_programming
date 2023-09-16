#!/usr/bin/python3
'''
    Script that lists all State objects from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine, insert
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
    query = insert(State).values(name="Louisiana")
    session.execute(query)
    session.commit()
    first_row = session.query(State).filter(State.name == "Louisiana").first()
    if first_row:
        print(first_row.id)
    session.close()
