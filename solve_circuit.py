from cholesky import solve
from util import vector_to_diag_matrix
from util import transpose
from util import mult
from pprint import pprint


def read_circuit_from_file(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()

    num_branches = int(lines[0])
    J = [[float(line.split(' ')[0])] for line in lines[1:1+num_branches]]
    y = [[1/float(line.split(' ')[1])] for line in lines[1:1+num_branches]]
    vector_to_diag_matrix(y) # pad with zeros to produce diagonal matrix
    E = [[float(line.split(' ')[2])] for line in lines[1:1+num_branches]]
    A = [[float(val) for val in line.split()] for line in lines[1+num_branches:]]

    A_transpose = transpose(A)

    pprint(A)
    pprint(y)
    pprint(A_transpose)
    pprint(mult(A, y))

    AyAt = mult(mult(A, y), A_transpose)

    pprint(AyAt)

    pprint(J)
    b = mult(A, J) #TODO add -JE

    pprint(b)
    pprint(solve(AyAt, b))

    # pprint(J)
    # pprint(E)
    # pprint(A)
    # pprint(y)

if __name__ == "__main__":
    read_circuit_from_file('circuit1.txt')
