#!/usr/bin/python3
"""
First user

"""
from models.base_models import BaseModel


class User(BaseModel):
    """ User that inherit from BaseModel """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
