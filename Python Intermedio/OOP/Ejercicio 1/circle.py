class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        import math        
        return math.pi * (self.radius ** 2)