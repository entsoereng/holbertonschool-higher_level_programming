#!/usr/bin/python3


"""Defines unittests for base.py."""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""
