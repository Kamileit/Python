class Complex:
    def __init__(self, real: int, imag: int):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __repr__(self):
        return "real: " + str(self.real) + " imag: " + str(self.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)


c1 = Complex(1, 1)
c2 = Complex(2, 2)
print(c1 * c2)
