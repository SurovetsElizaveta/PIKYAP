from lab_python_oop.geom_figure import GeomFigure
from lab_python_oop.figure_color import FigureColor

class Rectangle(GeomFigure):
    def __init__(self, wid, len, color):
        self.wid = wid
        self.len = len
        self.color = FigureColor(color)
        self.name = "Rectangle "

    def area(self):
        return self.wid * self.len

    def __repr__(self):
        return "{} Length: {} Width: {} Color: {}".format(self.get_name(), self.len, self.wid, self.color.get_color())

    def get_name(self):
        return self.name