#!/usr/bin/python3
#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ Place class """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship('Review', backref='place', cascade='all, delete')
