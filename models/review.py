#!/usr/bim/python3
"""
Public class attributes

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review that inherit from BaseModel """

    place_id = ''
    user_id = ''
    text = ''
