from Polynomial import Polynomial



def getRootsWithMultiplicityInInterval(polynomial, interval):
    roots = getRootsInInterval(polynomial, interval)

    rootsWithMultiplicity = []
    distinctRoots = findDistinctRoots(roots)

    for root in distinctRoots:
        multiplicity = 0

        for similarRoot in roots:
            if abs(root - similarRoot) < 10 ** (-1):
                multiplicity += 1

        rootsWithMultiplicity.append((root, multiplicity))

    return rootsWithMultiplicity


def findDistinctRoots(roots):
    distinctRoots = []

    for root in roots:
        if not isIn(root, distinctRoots):
            distinctRoots.append(root)

    return distinctRoots


def isIn(root, roots):
    for similarRoot in roots:
        if abs(similarRoot - root) <= 10**(-1):
            return True

    return False


def getRootsInInterval(polynomial, interval):
    poly = polynomial
    roots = []
    root = getRoot(polynomial, interval)

    while root is not None: # in case polynomial admit a root
        roots.append(root)
        poly = findQuotient(poly, root)
        root = getRoot(poly, interval)

    return roots


def getRoot(polynomial, interval):
    a, b = interval

    poly = polynomial.associatedFunction

    root = a

    for i in range(100): #à revoir le choix de 100 itération
        root = root - (poly(root) / d(poly, root))

        if abs(poly(root)) < 10**(-4):
            break

    if abs(poly(root)) < 10**(-3) and a <= root <= b:
        return root
    return


def d(function, x):
    return (function(x + 10**(-5)) - function(x)) / 10**(-5)


def findQuotient(polynomial, root):
    result = []

    if root == 0:
        for i in range(polynomial.degree):
            result.append(polynomial.getCoefficient(i + 1))
    else:
        result.append(-polynomial.getCoefficient(0) / root)

        for i in range(polynomial.degree):
            result.append((result[i] - polynomial.getCoefficient(i + 1)) / root)

    return Polynomial(result)

