from __future__ import print_function

from pprint import pprint
from math import sqrt
from util import mult
from util import equal


def decompose(A):
    L = [[0.0] * len(A) for _ in xrange(len(A))] # create L with same size as A
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else (1.0 / L[j][j] * (A[i][j] - s))
    return L


def forward_elimination(L, b):
    for j in xrange(len(L)):
        b[j][0] = b[j][0]/L[j][j]
        for i in range(j+1, len(L)):
            b[i][0] = b[i][0] - L[i][j]*b[j][0] # look ahead
    return b #actually y


def back_substitution(L, y):
    x = [[0.0] * len(y[0]) for _ in xrange(len(L))] # create x with same size as y
    for i in range(len(L)-1, -1, -1):
        sum = 0
        for j in range(i+1, len(L)):
            sum += L[j][i] * x[j][0]
        x[i][0] = (y[i][0] - sum) * 1.0 / L[i][i]
    return x

def solve(A, b):
    L = decompose(A)
    y = forward_elimination(L, b)
    x = back_substitution(L, y)
    return x

if __name__ == "__main__":
    A1 = [[25, 15, -5],
          [15, 18,  0],
          [-5,  0, 11]]
    x1 = [[1],
          [2],
          [3]]
    b1 = mult(A1, x1)

    pprint(equal(solve(A1, b1), x1))