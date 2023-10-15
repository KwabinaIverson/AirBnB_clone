#!/usr/bin/python3

"""
module: base_model
Holds one class, BaseModel()
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    The BaseModel class defines all command attributes or methods for other classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialization of objects
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'name' or key == 'my_number' or key == 'id':
                        self.key = value
                    else:  # format created_at & updated_at back to datetime objects
                        self.key = datetime.fromisoformat(value)
                    self.__dict__[key] = self.key
            if 'key' in self.__dict__:  # removes the key `key` from dict
                del self.__dict__['key']
        
        # If it's a new instance, add it to storage
        if not kwargs:
            storage.new(self)
        
    def __str__(self):
        """
        Should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
            By using self.__dict__, only instance attributes set will be returned.
            A key __class__ must be added to this dictionary with the class name of the object.
            
            created_at and updated_at must be converted to string object in ISO format:
                format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259).
                You can use isoformat() of datetime object.
        """
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
