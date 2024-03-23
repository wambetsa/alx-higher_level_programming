#!/usr/bin/python3
"""
    a python file similar to model_state.py
    city class inherits from base
    links to mysql table
"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class City(Base):
    """
        class City inheriting from Base
        class attributes:
            id - clumn, auto-generated, int, not null, pk
            name - column, string, chars = 128, not null
            state_id - column, integer, not null, foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

