from util import print_mat
from solve_circuit import read_circuit_from_file
from solve_circuit import solve_circuit


def connect_last_node_to_first(incidence_matrix):
    for ind, value in enumerate(incidence_matrix[1]):
        if value != 0:
            incidence_matrix[-1][ind] = value


def remove_unnecessary_data(incidence_matrix):
    del incidence_matrix[0]
    for row in incidence_matrix:
        del row[0]
    del incidence_matrix[0]
    del incidence_matrix[-1] # TO GET REDUCED


# Generate a Nx2N linear resistor network with 1kOhm resistors and a 10V external voltage source that connects the
# bottom left and top right corners
def generate_circuit_file(N):
    num_branches = 8 * ((N + 1) * N) / 2 - N  # 8*[Sum from i to N] - N
    num_nodes = (2 * N + 1) * (N + 1)
    incidence_matrix = [[0 for x in xrange(num_branches + 1)] for x in xrange(num_nodes + 1)]
    for j in range(1, (N+1)*2*N +1):
        num_rows_before = (j - 1) / (2 * N)
        incidence_matrix[j + num_rows_before][j] = 1
        incidence_matrix[j + num_rows_before + 1][j] = -1

    for j in range((N+1)*2*N+1, num_branches+1):
        num_cols_before = (N+1)*2*N
        incidence_matrix[j - num_cols_before][j] = 1
        incidence_matrix[j - num_cols_before + (2*N + 1)][j] = -1

    connect_last_node_to_first(incidence_matrix)
    remove_unnecessary_data(incidence_matrix)

    print_mat(incidence_matrix)

    jre_matrix = [[0 for x in xrange(3)] for x in xrange(num_branches)]
    for i in xrange(num_branches):
        jre_matrix[i][1] = 1000

    jre_matrix[0][2] = 10
    jre_matrix[num_branches / 2 + 1][2] = 10

    filename = "linearResistorNetwork{}x{}.txt".format(N, 2*N)
    with open(filename, 'w') as f:
        f.write(str(num_branches)+"\n")
        f.write(format_matrix_for_file(jre_matrix)+"\n")
        f.write(format_matrix_for_file(incidence_matrix))

    return filename, num_branches


def format_matrix_for_file(matrix):
    string = ""
    for row in matrix:
        for number in row:
            string += str(number) + " "
        string += "\n"
    return string.rstrip()


if __name__ == '__main__':
    N = 2
    filename, num_branches = generate_circuit_file(N)
    J, y, E, A = read_circuit_from_file(filename)
    Vn = solve_circuit(J, y, E, A)
    total_current = (10-Vn[0][0])/1000 + (10-Vn[2*N][0])/1000
    print 10/total_current