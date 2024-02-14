#!/usr/bin/python3
"""
Defines a base model class.
"""
Class Base:
    """
    Represents the base model.
    """
    __nb_objects = 0
    def __init__(self, id=none):
        if id is not none:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
