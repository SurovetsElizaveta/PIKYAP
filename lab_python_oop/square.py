from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    def __int__(self, len, color):
        self.side = len
        super().__init__(self.side, self.side, color)
        self.name = "Square "

    def area(self):
        return self.len * self.len

    def __repr__(self):
        return "{} Side: {} Color: {}".format(self.get_name_square(), self.len, self.color.get_color())

    def get_name_square(self):
        return self.name