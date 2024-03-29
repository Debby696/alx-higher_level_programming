#!/usr/bin/python3

"""a python file named model_city.py that contains
the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
