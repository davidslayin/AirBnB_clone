#!/usr/bin/python3

"""
Module review
Contain class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that represent Review
    Attributes
    ----------
    place_id = ""
        unique identification of the place
    user_id = ""
        unique identification of the user
    text : str
        Contain information
    """
    place_id = ""
    user_id = ""
    text = ""
