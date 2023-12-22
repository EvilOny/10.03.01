import unittest
from unit_tests.GeometricalFigues import Triangle, Rectangle


class TestGeometryFigures(unittest.TestCase):
    def test_triangle_pl(self):
                triangle = Triangle('Треугольник', 5, 3, 4)
                triangle.square()
                self.assertEqual(triangle.square(), 'Площадь Треугольника: 6.0')

    def test_rectangle_pl(self):
        rectangle = Rectangle('Прямоугольник', 9, 2)
        rectangle.square()
        self.assertEqual(rectangle.square(), 'Площадь Прямоугольника: 18')


if __name__ == '__main__':
    unittest.main()
