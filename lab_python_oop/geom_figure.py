from abc import ABC, abstractmethod

class GeomFigure(ABC):

    @abstractmethod
    def area(self):
        pass
