#!/usr/bin/python3
"""
Module file_storage
Contain class FileStorage
This script serve as a file storage engine.
This file can also be imported as a module and contains the following
functions:
    * all - returns a dictionary of all created object
    * new - sets newly created object with key object.id to __objects
    * save - serializes __objects to the JSON file
    * reload - deserializes the JSON file to __objects
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User


class FileStorage:
    """class that represent FileStorage
    Attributes
    ----------
    __file_path : str
            Contain file path name
    __objects : dict
            Contain a dictionary of object with key object.id
    class_dict : dict
            Contain available classes
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "Amenity": Amenity, "Place": Place, "City": City,
                  "Review": Review}

    def all(self):
        """reterive the dictionary __objects
        Returns
        -------
        dict
            All created collection of different objects
        """
        return self.__objects

    def new(self, obj):
        """sets newly created object with key object.id to __objects"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_dic = {}
        for key, obj in self.__objects.items():
            my_dic[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_dic, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
