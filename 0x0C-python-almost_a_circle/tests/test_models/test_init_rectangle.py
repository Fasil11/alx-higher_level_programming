#!/usr//bin/python3
"""
Unitest for rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.square import square
from  models.base import Base



class TestRectangle(unittest.TestCase):
    """
    test for Rectangle
    """

   def test_rectangle_is_instance_of_base(self):
       """ test for if the rect is instance of Base """

       r1 = Rectangle(10, 2, 0, 0, 12)
       self.assertISInstance(r1, Base)


    def test_value_is_int(self):
        """Test if the value for init is an int"""
        with self.assertRaise(TypeError):
            r1 = Rectangle("f", "f", "f", "f")

    def test_value_is_negative(self):
        """test if the val is neg """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 1, -1, 12)

    def test_value_is_not_tuple(self):
        """test W and H with tuples"""
        with self.assertRaises(TypeError)
        r2 = Rectangle(1, -10, -2, (1,10) -12)
    
    def test_value_is_not_list(self):
        """test W and H with list """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [1, -10], 12)

    def test_value_is_not_dict(Self):
        """test W with dict """
        with self.assertRaises(TypeError):
            r2 = Rectanle(2, 2, 2, {'lolo': -10}, 12)

    def test_value_is_not_empty(Self):
        """test empy instance """
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_display_None(self):
        """test with alone"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)

    def test_x_setter(self):
       """Test x setter"""
        r = Rectangle(5, 7, 0, 0, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(5, 7, 30, 30, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_x_setter_neg(self):
        """Test x setter neg"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 7, 30, 30, 1)
            r.x = -10

    def test_y_setter_neg(self):
        """Test y setter negative"""
        with self.assertRaises(ValueError):
            r Rectangle(5, 7, 10, 30, 1)
            r.y = -10
    
    def test_x_setter_string(self):
        """Test x setter string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = "lolo"

    def test_y_setter_string(self):
        """Test y setter string"""
        with self.



