from __future__ import print_function

from pprint import pprint
from math import sqrt
from util import transpose
from util import mult


def decompose(A):
    L = [[0.0] * len(A) for _ in xrange(len(A))] # create L with same size as A
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else (1.0 / L[j][j] * (A[i][j] - s))
    return L


def forward_elim(L, b):
    for j in xrange(len(L)):
        b[j] = b[j]/L[j][j]
        for i in range(j+1, len(L)+1):
            b[i] = b[i] - L[i][j]*b[j] # look ahead
    return b #actually y


def back_substitution(L, y):
    x = [[0.0] * len(y) for _ in xrange(len(y))] # create x with same size as y
    for i in range(len(L)-1, -1, -1):
        sum = 0
        for j in range(i+1, len(L)):
            sum += L[j][i] * x[j]
        x[i] = (y[i] - sum) * 1.0 / L[i][i]
    return x


if __name__ == "__main__":
    A1 = [[25, 15, -5],
          [15, 18,  0],
          [-5,  0, 11]]
    x1 = [[1],
          [2],
          [3]]
    b1 = mult(A1, x1)
    pprint(b1)



    l1 = decompose(A1)
    pprint(l1)

    l1transpose = transpose(l1)
    pprint(l1transpose)

    product = mult(l1, l1transpose)
    pprint(product) # SAME AS A --> DECOMPOSITION SUCCESSFUL!

    m2 = [[18, 22,  54,  42],
          [22, 70,  86,  62],
          [54, 86, 174, 134],
          [42, 62, 134, 106]]
    pprint(decompose(m2), width=120)