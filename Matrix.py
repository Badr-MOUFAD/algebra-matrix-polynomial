from Polynomial import Polynomial


class Matrix:
    def __init__(self, array):
        self._matrix = array

        if not Matrix.isColumnMatrix(self):
            for row in self._matrix:
                if len(row) != len(self[0]):
                    raise Exception("Declaration error: \n Rows must have same number of items")

        try:  # case matrix (n, p)
            for i in range(len(self._matrix)):
                for j in range(len(self[i])):
                    if not isinstance(self[i][j], Polynomial):
                        self[i][j] = Polynomial([self[i][j]])

            self.__nbRows = len(self._matrix)
            self.__nbColumns = len(self[0])
        except TypeError:  # case column matrix
            for element in self._matrix:
                if not isinstance(element, Polynomial):
                    element = Polynomial([element])

            self.__nbRows = len(self._matrix)
            self.__nbColumns = 1

        return

    @property
    def nbRows(self):
        return self.__nbRows

    @property
    def nbColumns(self):
        return self.__nbColumns

    def getSubMatrix(self, iRow, jColumn):
        if Matrix.isColumnMatrix(self):
            return
        if self.nbRows <= iRow < 0:
            return
        if self.nbColumns <= jColumn < 0:
            return

        result = []
        for i in range(len(self._matrix)):
            result.append(list(self._matrix[i]))

        result.pop(iRow)

        for i in range(len(result)):
            result[i].pop(jColumn)

        return Matrix(result)

    # enable indexing
    def __getitem__(self, item):
        try:
            return self._matrix[item]
        except IndexError:
            print(len(self._matrix))

    def __setitem__(self, row, value):
        self._matrix[row] = value

    # print matrix
    def __str__(self):
        stringMatrix = ""

        if Matrix.isColumnMatrix(self):
            for i in range(self.nbRows):
                stringMatrix += str(self[i]) + "\t" * 5

            return stringMatrix

        for i in range(self.nbRows):
            for j in range(self.nbColumns):
                stringMatrix += str(self[i][j]) + "\t" * 5
            stringMatrix += '\n'

        return stringMatrix

    def __add__(self, other):
        if self.nbColumns != other.nbColumns or self.nbRows != other.nbRows:
            raise Exception("Dimension error \nMatrix must have same dimension")

        result = Matrix.zeros(self.nbRows, self.nbColumns)
        for i in range(result.nbRows):
            for j in range(result.nbColumns):
                result[i][j] = self[i][j] + other[i][j]

        return result

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if other.nbRows != self.nbColumns:
                raise Exception("Dimension error \nIn multiplication matrices must have dimensions (n, p) * (p, k)")

            result = Matrix.zeros(self.nbRows, other.nbColumns)

            for i in range(result.nbColumns):
                for j in range(result.nbRows):
                    for k in range(self.nbColumns):
                        result[i][j] += self[i][k] * other[k][j]

            return result

        result = Matrix.zeros(self.nbRows, self.nbColumns)
        for i in range(result.nbRows):
            for j in range(result.nbColumns):
                result[i][j] = other * self[i][j]

        return result

    def __rmul__(self, other):
        return self * other

    @staticmethod
    def isColumnMatrix(matrix):
        try:
            matrix[0][0]
        except TypeError:
            return True

        return False

    @staticmethod
    def zeros(nbRows, nbColumns, fillWith=0):
        matrix = []

        for i in range(nbRows):
            row = []
            for j in range(nbColumns):
                row.append(fillWith)
            matrix.append(row)

        return Matrix(matrix)

    @staticmethod
    def transpose(matrix):
        if Matrix.isColumnMatrix(matrix):
            return Matrix([[matrix[i] for i in range(matrix.nbRows)]])

        result = Matrix.zeros(matrix.nbColumns, matrix.nbRows)

        for i in range(matrix.nbRows):
            for j in range(matrix.nbColumns):
                result[j][i] = matrix[i][j]

        return result