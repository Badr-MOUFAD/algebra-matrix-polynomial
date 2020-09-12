
class Polynomial:
    def __init__(self, coefficients):
        self.__coefficients = coefficients

        # removing eventual zeros from the end of the list ([1, 2, 0, 0] == [1, 2])
        j = len(self.__coefficients) - 1
        while self.__coefficients[j] == 0:
            if j == 0: # case of a null polynomial (like [0] or [0, 0, 0])
                break
            self.__coefficients.pop(j)
            j -= 1

        self.__degree = len(self.__coefficients) - 1

        def f(x):
            result = 0

            for i in range(self.degree + 1):
                result += self.getCoefficient(i) * x**i

            return result

        self.__associatedFunction = f
        return

    @property
    def degree(self):
        return self.__degree

    @property
    def associatedFunction(self):
        return self.__associatedFunction

    def getCoefficient(self, index):
        if index < 0:
            return
        if index >= len(self.__coefficients):
            return 0

        return self.__coefficients[index]
    # in order to print to polynomial
    def __str__(self):
        if self.degree == 0:
            return "{0:0.2f}".format(self.getCoefficient(self.degree))

        polynomial = "" if self.getCoefficient(0) == 0 else "{0:0.2f} + ".format(self.getCoefficient(0))

        for i in range(1, self.degree):
            if self.getCoefficient(i) != 0:
                polynomial += "{0:0.2f} X^{1} + ".format(self.getCoefficient(i), i)

        polynomial += "{0:0.2f} X^{1}".format(self.getCoefficient(self.degree), self.degree)

        return polynomial
    # custum operations
    def __add__(self, other):
        result = []

        for i in range(max(self.degree, other.degree) + 1):
            result.append(self.getCoefficient(i) + other.getCoefficient(i))

        return Polynomial(result)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            from Matrix import Matrix

            result = Matrix.zeros(other.nbRows, other.nbColumns)

            for i in range(result.nbRows):
                for j in range(result.nbColumns):
                    result[i][j] = self * other[i][j]

                return result

        result = []

        for i in range(self.degree + other.degree + 1):
            coeff = 0

            for j in range(i + 1):
                coeff += self.getCoefficient(j) * other.getCoefficient(i - j)

            result.append(coeff)

        return Polynomial(result)

    def __sub__(self, other):
        other_ = Polynomial([-1]) * other

        return self + other_