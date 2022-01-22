class Animal:
    def __init__(self, color, speed, diet_type, name, size):
        self.color = color
        self.speed = speed
        self.diet_type = diet_type
        self.name = name
        self.size = size
    
    def eat(self):
        print(f"{self.name} the is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")
    