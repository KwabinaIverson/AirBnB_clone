#!/usr/bin/python3
"""User class that inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """Defination of User class"""

    def __init__(self, *args, **kwargs):
	"""Initialization of class attributes"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
