from Lab1.lab_python_oop.rectangle import Rectangle
from Lab1.lab_python_oop.circle import Circle
from Lab1.lab_python_oop.square import Square

def main():
    n = 10
    rect = Rectangle(n, n, "blue")
    circ = Circle(n, "green")
    sqr = Square(n, n, "red")
    print(rect.__repr__())
    print(circ.__repr__())
    print(sqr.__repr__())

if __name__ == '__main__':
    main()