from lab_python_oop.geom_figure import GeomFigure
from lab_python_oop.figure_color import FigureColor
from math import pi

class Circle(GeomFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)
        self.name = "Circle "

    def area(self):
        return 2 * pi * self.radius

    def __repr__(self):
        return "{} Radius: {} Color: {}".format(self.get_name(), self.radius, self.color.get_color())

    def get_name(self):
        return self.name