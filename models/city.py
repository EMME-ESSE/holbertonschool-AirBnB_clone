#!/usr/bin/python3
"""
Public class attributes

"""
from models.base_model import BaseModel


class City(BaseModel):
    """  City that inherit from BaseModel """

    state_id = ''
    name = ''
