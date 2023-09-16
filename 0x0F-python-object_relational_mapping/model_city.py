#!/usr/bin/python3
'''
    Class definition of the City
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
        Initialisation of the class State
    '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
