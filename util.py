from prettytable import PrettyTable
import math


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
    if type(A[0]) is float:
        return [A[i] - B[i] for i in xrange(len(A))]
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ArithmeticError("Size of matrices don't match!")
    else:
        result = [[0 for x in xrange(len(A[0]))] for x in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                result[i][j] += A[i][j] - B[i][j]
        return result


def scalar_mult(A, c):
    result = [[A[i][j] for j in xrange(len(A[0]))] for i in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(len(A[i])):
            result[i][j] *= c
    return result


def mult(A, B):
    result = [[0 for x in xrange(len(B[0]))] for x in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def norm(v, p):
    result = 0
    if p == 1:
        for num in v:
            num = num[0]
            result += abs(num)
    elif p == 2:
        for num in v:
            num = num[0]
            result += num*num
        result = math.sqrt(result)
    elif p == 'inf':
        max = abs(v[0][0])
        for num in v:
            num_abs = abs(num[0])
            if num_abs > max:
                max = num_abs
        result = max
    return result


def cross(v1, v2): # 2D cross product
    return v1[0]*v2[1]-v1[1]*v2[0]


def dot(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError("Size of vectors don't match!")
    else:
        sum = 0
        for i in xrange(len(v1)):
            sum += (v1[i] * v2[i])
        return sum


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

if __name__ == '__main__':
    a = [[2, 2.2, 3.3],
     [-1, 32.2, 2]]

    print_mat(scalar_mult(a, 5))