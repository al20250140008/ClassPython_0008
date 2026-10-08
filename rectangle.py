class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar tidak boleh 0 atau negatif!")
        self.length = length
        self.width = width
    def circumference(self):
        return 2 * (self.length + self.width)
     def area(self):
        return self.length * self.width
    