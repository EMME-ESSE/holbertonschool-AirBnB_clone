#!/usr/bim/python3
"""
Public class attributes

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place that inherit from BaseModel """

    city_id = ''
    user = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []