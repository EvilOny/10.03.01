class GeometricalFigure:
    def __init__(self, name):
        self.name = name


class Triangle(GeometricalFigure):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        pl = pow((p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 0.5)
        triangle_square = f'Площадь {self.name}а: {pl}'

        return triangle_square


class Rectangle(GeometricalFigure):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def square(self):
        rectangle_square = f'Площадь {self.name}а: {self.width * self.height}'

        return rectangle_square
