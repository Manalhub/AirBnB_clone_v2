#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

'''storage_type = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})

    name = Column(
        String(128), nullable=False
    ) if storage_type == 'db' else ''

    if storage_type == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            from models.city import City

            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state

'''
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with state_id
            equals to the current State.id"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
