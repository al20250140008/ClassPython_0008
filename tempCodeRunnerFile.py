class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar tidak boleh 0 atau negatif!")
        self.length = length
        self.width = width