from prettytable import PrettyTable


def transpose(A):
    return [list(x) for x in zip(*A)]


def add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ArithmeticError("Size of matrices don't match!")
    else:
        result = [[0 for x in xrange(len(A[0]))] for x in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                result[i][j] += A[i][j] + B[i][j]
        return result


def subtract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ArithmeticError("Size of matrices don't match!")
    else:
        result = [[0 for x in xrange(len(A[0]))] for x in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                result[i][j] += A[i][j] - B[i][j]
        return result


def mult(A, B):
    result = [[0 for x in xrange(len(B[0]))] for x in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def equal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    else:
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if abs(A[i][j] - B[i][j]) > 0.000001:
                    return False
    return True


def vector_to_diag_matrix(vector):
    diag = [[e for e in innerlist] for innerlist in vector]
    for idx, val in enumerate(diag):  # Make y diagonal
        for i in xrange(len(diag) - 1 - idx):
            val.append(0)
        for i in xrange(idx):
            val.insert(0, 0)
    return diag


# Inspired by http://codegolf.stackexchange.com/questions/8405/matrix-determinant
def det(x):
    l = len(x)
    if l == 1:
        return x[0][0]
    return sum([(-1) ** i * x[i][0] * det(minor(x, i + 1, 1)) for i in range(l)])


# Inspired by http://codegolf.stackexchange.com/questions/8405/matrix-determinant
def minor(x, i, j):
    y = x[:]
    del (y[i - 1])
    y = zip(*y)
    del (y[j - 1])
    return zip(*y)


def print_mat(matrix):
    print format_mat(matrix)


def format_mat(matrix):
    p = PrettyTable()
    for row in matrix:
        p.add_row(row)

    return p.get_string(header=False, border=False)