#!/usr/bin/python3
"""
Base Class that defines all common attributes/methods for other classes.
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Custom base for all the classes in the AirBnb console project.

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

    def __init__(self, *args, **kwargs):
        """
        Method initializes the BaseModel attributes using args and kwargs.
        """
        if kwargs:
            D_TIME = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], D_TIME)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Method returns string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method updates updated_at attribute with the current datetime.
        """
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Method return dictionary representation of BaseModel instance.
        """
        object_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                object_dict[key] = value.isoformat()
            else:
                object_dict[key] = value
        object_dict["__class__"] = self.__class__.__name__

        return object_dict
