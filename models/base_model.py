#!/usr/bin/python3
"""
Module base_model
Contain class BaseModel
This script serve as a base class for other class.
This file can also be imported as a module and contains the following
functions:
    * save - updates the public instance attribute and call save method from
             from filestorage
    * to_dict - returns a dictionary containing all keys/values of __dict__ of
              the instance
    * __str__ - print string representation of an object
"""

import uuid
from datetime import datetime as dt
import models


class BaseModel:
    """ class that represent BaseModel
    Attributes
    -----------
    id : int
            unique identification
    created_at : datetime
            date the instance created
    updated_at : datetime
            date the instance updated
    Methods
    -------
    save()
        updates the public instance attribute updated_at
        with the current datetime
    to_dict():
        return a dictionary containing all keys/values of
        __dict__ of the instance
    Gen Info
    ---------
        :param **kwargs: Optionally accepts named arguments
        :type **kwargs: The type can be any type including datetime
        :raise TypeError: If date formate is not convertible
        :return: has no return
        :rtype: None
    """

    def __init__(self, *args, **kwargs):
        """initialize attribute
        Parameters
        -----------
        id : int
                unique identification
        created_at : datetime
                date the instance created
        updated_at : datetime
                date the instance updated
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == "updated_at":
                    self.updated_at = dt.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.created_at = dt.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.utcnow()
            self.updated_at = dt.utcnow()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = dt.utcnow()
        models.storage.save()

    def to_dict(self):
        """reterive a dictionary containing all keys/values of __dict__
        of the instance
        Returns
        -------
        dict
            a dictionary containing all/values of __dict__ of the instance
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        return dic

    def __str__(self):
        """reterive informal string representation of an instance
        Returns
        -------
        str
            string representation containing instance class, id and dictionary
        """
        string_rep = "[{}] ({}) {}".format(self.__class__.__name__,
                                           self.id, self.__dict__)
        return string_rep
