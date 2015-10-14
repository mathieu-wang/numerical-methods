from cholesky import solve
from pprint import pprint

def read_circuit_from_file(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()

    num_branches = int(lines[0])
    J = [[float(line.split(' ')[0])] for line in lines[1:1+num_branches]]
    R = [[float(line.split(' ')[1])] for line in lines[1:1+num_branches]]
    E = [[float(line.split(' ')[2])] for line in lines[1:1+num_branches]]
    A = [[float(val) for val in line.split()] for line in lines[1+num_branches:]]
    pprint(J)
    pprint(R)
    pprint(E)
    pprint(A)

if __name__ == "__main__":
    read_circuit_from_file('circuit1.txt')
