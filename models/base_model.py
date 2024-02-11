#!/usr/bin/python3
"""
Base Class that defines all common attributes/methods for other classes.
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Custom base for all the classes in the AirBnb console project.

    Attributes:
        id(str): assign with an uuid when an instance is created.
        created_at(datetime): assign current datetime when
        an instance is created.
        updated_at(datetime): assign with current datetime when an instance is
        created and it will be updated every time you change your object.

    Methods:
        __str__: prints `[<class name>] (<self.id>) <self.__dict__>`
        the class name, id, and creates dictionary representations
        .of the input values
        save(self): updates instance attributes with current datetime
        to_dict(self): returns a dictionary containing all keys/values of
        `__dict__` of the instance.

    """
    def __init__(self):
        """Method initializes the BaseModel attributes."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Method returns string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Method updates updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method return dictionary representation of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
