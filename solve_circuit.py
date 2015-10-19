from cholesky import solve
from cholesky import solve_with_band
from util import vector_to_diag_matrix
from util import transpose
from util import subtract
from util import mult
from util import print_mat
from pprint import pprint


def read_circuit_from_file(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()
        # print "circuit file:"
        # for line in lines:
        #     print line,


    num_branches = int(lines[0])
    J = [[float(line.split(' ')[0])] for line in lines[1:1+num_branches]]
    R_inv = [[1/float(line.split(' ')[1])] for line in lines[1:1+num_branches]]
    y = vector_to_diag_matrix(R_inv) # pad with zeros to produce diagonal matrix
    E = [[float(line.split(' ')[2])] for line in lines[1:1+num_branches]]
    A = [[float(val) for val in line.split()] for line in lines[1+num_branches:]]

    return J, y, E, A


def solve_circuit(J, y, E, A):
    A_transpose = transpose(A)

    AyAt = mult(mult(A, y), A_transpose)

    b = mult(A, subtract(J, mult(y, E)))
    Vn = solve(AyAt, b)
    return Vn


def solve_circuit_with_band(J, y, E, A, half_bandwidth):
    A_transpose = transpose(A)

    AyAt = mult(mult(A, y), A_transpose)

    b = mult(A, subtract(J, mult(y, E)))
    Vn = solve_with_band(AyAt, b, half_bandwidth)
    return Vn


if __name__ == "__main__":
    J, y, E, A = read_circuit_from_file('circuit1.txt')
    Vn = solve_circuit(J, y, E, A)
    print "\n\nJ:"
    print_mat(J)
    print "y:"
    print_mat(y)
    print "E:"
    print_mat(E)
    print "A:"
    print_mat(A)
    print "Vn = solve(AyAt, A(J-yE)):"
    print_mat(Vn)
    # Vn = solve_circuit_with_band(J, y, E, A, 2)
    # pprint(Vn)
