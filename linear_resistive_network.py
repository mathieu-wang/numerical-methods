from util import print_mat
from util import format_mat


def connect_last_node_to_first(matrix):
    for ind, value in enumerate(matrix[-1]):
        if value != 0:
            matrix[1][ind] = value


def remove_unnecessary_data(matrix):
    del matrix[0]
    del matrix[-1]
    for row in matrix:
        del row[0]


# Generate a Nx2N linear resistor network with 1kOhm resistors and a 10V external voltage source that connects the
# bottom left and top right corners
def generate_circuit_file(N):
    num_branches = 8 * ((N + 1) * N) / 2 - N  # 8*[Sum from i to N] - N
    num_nodes = (2 * N + 1) * (N + 1)
    matrix = [[0 for x in xrange(num_branches + 1)] for x in xrange(num_nodes + 1)]
    for j in range(1, num_branches / 2 + 2):
        matrix[j + (j - 1) / (2 * N)][j] = 1
        matrix[j + (j - 1) / (2 * N) + 1][j] = -1

    for j in range(num_branches / 2 + 2, num_branches + 1):
        matrix[j - num_branches / 2 - 1][j] = 1
        matrix[j - num_branches / 2 - 1 + (2*N + 1)][j] = -1

    connect_last_node_to_first(matrix)
    remove_unnecessary_data(matrix)

    print_mat(matrix)

    with open("linearResistorNetwork{}x{}.txt".format(N, 2*N), 'w') as f:
        f.write(str(num_branches)+"\n")
        f.write(format_mat(matrix))


if __name__ == '__main__':
    generate_circuit_file(2)
