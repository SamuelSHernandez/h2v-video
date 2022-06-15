from unittest import TestCase

from app.resize import new_height, new_width

class TestResize(TestCase):

    def __init__(self):
        self.new_width = 520
        self.new_height = 1080

    TestCase.assertEqual(new_height, 1080)
    TestCase.assertEqual(new_width, 520)  
