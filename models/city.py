#!/usr/bin/python3

"""
Module city
Contain class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class that represent city
    Attributes
    ----------
    stste_id : str
        unique identification of the city
    name : str
        The name of the city
    """
    state_id = ""
    name = ""
