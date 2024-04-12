#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """Represents a state for a SQL database."""
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
    #@property
    #def cities(self):
    #    """Getter attribute cities that
    #eturns the list of City instances"""
        #city_list = []
        #all_cities = models.storage.all(City)
        #for city in all_cities.values():
        #    if city.state_id == self.id:
        #   city_list.append(city)
        #return city_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Gets a list of City instances with state_id matching this State's id."""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]

        def close(self):
            """Close session"""
            Session.close()