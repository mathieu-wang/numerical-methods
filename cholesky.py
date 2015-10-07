from __future__ import print_function

from pprint import pprint
from math import sqrt
from util import transpose
from util import mult


def decompose(A):
    L = [[0.0] * len(A) for _ in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else (1.0 / L[j][j] * (A[i][j] - s))
    return L

def forward_elim(L, b):
    for j in xrange(len(L)):
        b[j] = b[j]/L[j][j]
        for i in range(j+1, len(L)):
            b[i] = b[i] - L[i][j]*b[j] # look ahead

def back_substitution():
    pass

if __name__ == "__main__":
    m1 = [[25, 15, -5],
          [15, 18,  0],
          [-5,  0, 11]]

    l1 = decompose(m1)
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