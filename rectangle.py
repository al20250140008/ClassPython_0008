class Rectangle:
    """Persegi panjang dengan properti length (panjang) dan width (lebar)."""

    def __init__(self, length, width):
        # Nilai input tidak boleh 0 (atau negatif)
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar tidak boleh 0 atau negatif!")
        self.length = length
        self.width = width

    def circumference(self):
        """Keliling = 2 x (panjang + lebar)"""
        return 2 * (self.length + self.width)

    def area(self):
        """Luas = panjang x lebar"""
        return self.length * self.width

    def __str__(self):
        return f"Persegi panjang, panjang {self.length} cm dan lebar {self.width} cm"