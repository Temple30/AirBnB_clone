#!/usr/bin/python3
"""
UniqueBaseModel - Module
Parent class for unique BaseModel,
 """

import unique_id_generator
from unique_datetime import UniqueDateTime
import unique_models as models


class UniqueBaseModel:
    """
    UniqueBaseModel class serves as the parent class for unique initialization,
    serialization, and deserialization of instances.
    """
    def __init__(self, *args, **kwargs):
        """Initialization of a UniqueBaseModel instance"""
        if not kwargs:
            self.id = unique_id_generator.generate_id()
            self.created_at = UniqueDateTime.now()
            self.updated_at = UniqueDateTime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = UniqueDateTime.strptime(kwargs["created_at"])
            kwargs["updated_at"] = UniqueDateTime.strptime(kwargs["updated_at"])
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """String representation of a UniqueBaseModel instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
        Return string representation of UniqueBaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates 'updated_at' instance with current datetime"""
        self.updated_at = UniqueDateTime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of UniqueBaseModel class."""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime()
        new_dict['updated_at'] = self.updated_at.strftime()

        return new_dict

