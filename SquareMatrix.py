from Matrix import Matrix
from Polynomial import Polynomial
from rootPolynomial import getRootsInInterval, findDistinctRoots


class SquareMatrix(Matrix):
    def __init__(self, array):
        super().__init__(array)

        if self.nbRows != self.nbColumns:
            raise Exception("Decleration error:\n Square matrices haves number of rows identical to number of columns.")

        self.dimension = self.nbRows
        return

    def isInv(self):
        return

    def inv(self):
        return

    def com(self):
        return

    def getSpectrum(self):
        characteristicPolynomial = self.characteristicPolynomial()
        roots = getRootsInInterval(characteristicPolynomial, [-1000, 1000])

        eigenValues = findDistinctRoots(roots)
        return eigenValues

    def characteristicPolynomial(self):
        X = Polynomial([0, -1])
        n = self.dimension

        return SquareMatrix.det(self + SquareMatrix.identity(n) * X)

    @staticmethod
    def det(matrix):
        if matrix.nbRows != matrix.nbColumns:
            raise Exception("Operation error:\n det is special to square matrices.")

        result = Polynomial([0])

        if matrix.nbRows == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        for i in range(matrix.nbRows):
            subMatrix = matrix.getSubMatrix(i, 0)
            result += SquareMatrix.det(subMatrix) * Polynomial([(-1) ** (1 + i)]) * matrix[i][0]

        return result

    @staticmethod
    def identity(dimension):
        result = Matrix.zeros(dimension, dimension)

        for i in range(dimension):
            result[i][i] = Polynomial([1])

        return SquareMatrix(result._matrix)