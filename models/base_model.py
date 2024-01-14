#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
import models
from uuid
from datetime import datetime


class BaseModel:
    """
    Represents the BaseModel of the HBnB project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], dtime_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], dtime_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """
        Update updated_at with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        _dict = self.__dict__.copy()
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["__class__"] = self.__class__.__name__
        return _dict
