from mimetypes import init
from animal import Animal

class Fish(Animal):
    def __init__(self, color, speed, diet_type, name, size):
        super().__init__(color, speed, diet_type, name, size)
        