#!/usr/bin/python3

"""
Module place
Contain class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class that represent place
    Attributes
    ----------
    city_id : str
        unique identification of the city
    user_id : str
        unique identification of the user
    name : str
        The name of the place
    description : str
        Description of the place
    number_rooms : int
        The number of the room
    number_bathrooms : int
        The number of the bathroom
    max_guest : int
        The maximum holding capacity of the room
    price_by_night : int
        The price of the room per night
    latitude : float
        The latitude of the place
    longitude : float
        The longitude of the place
    amenity_ids : list
        A list contain amenity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
