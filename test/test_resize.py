from typing_extensions import assert_type
from unittest import TestCase

"""
Test
"""
from app.resize import new_height, new_width
class TestResize(TestCase):
    """
    Test
    """
    def __init__(self):
        self.new_height = 1080
        self.new_width  = 520

    TestCase.assertEqual(new_height, 1080)
    TestCase.assertEqual(new_width, 520)    
