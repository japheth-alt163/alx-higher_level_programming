import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_width_getter(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)

    def test_width_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

    def test_width_setter_non_integer(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rectangle.width = "hello"

    def test_width_setter_negative(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rectangle.width = -5

    def test_height_getter(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.height, 20)

    def test_height_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.height = 30
        self.assertEqual(rectangle.height, 30)

    def test_height_setter_non_integer(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rectangle.height = "hello"

    def test_height_setter_negative(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rectangle.height = -5

    def test_x_getter(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.x, 0)

    def test_x_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_x_setter_non_integer(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rectangle.x = "hello"

    def test_x_setter_negative(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rectangle.x = -5

    def test_y_getter(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.y, 0)

    def test_y_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.y = 10
        self.assertEqual(rectangle.y, 10)

    def test_y_setter_non_integer(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rectangle.y = "hello"

    def test_y_setter_negative(self):
        rectangle = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rectangle.y = -5

    def test_area(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.area(), 200)

    def test_display(self):
        rectangle = Rectangle(5, 3)
        expected_output = "\n\n###"
        self.assertEqual(rectangle.display(), expected_output)

    def test_str(self):
        rectangle = Rectangle(10, 20, 5, 2)
        expected_output = "[Rectangle] (1) 5/2 - 10/20"
        self.assertEqual(str(rectangle), expected_output)

    def test_update(self):
        rectangle = Rectangle(10, 20)
        rectangle.update(15, 30, 2, 5)
        self.assertEqual(rectangle.id, 15)
        self.assertEqual(rectangle.width, 30)


if __name__ == "__main__":
    unittest.main()
