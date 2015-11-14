from finite_difference_methods import cg
from finite_difference_methods import sor
from finite_difference_methods import jacobi
from cholesky import solve
from util import print_mat
from util import transpose
from util import mult


def find_potential_at_point(potential_matrix, x_coord, y_coord):
    node_x = int(x_coord / h)
    node_y = int(y_coord / h)
    return potential_matrix[node_x][node_y]


def setup_matrix_equation():
    A = [[-4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, -4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, -4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, -4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, -4, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, -4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, -4, 2, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -4, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -4]]

    b = [[-10],
         [0],
         [-10],
         [0],
         [-10],
         [-10],
         [-10],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0]]

    indices = [2, 3, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]

    initial_x = [[0] for _ in xrange(19)]

    return A, initial_x, b, indices


def get_potential_at_node(potentials, indices, node):  # Using binary search
    left = 0
    right = len(indices) - 1
    while True:
        mid = left + (right - left) / 2
        if indices[mid] < node:
            left = mid + 1
        elif indices[mid] > node:
            right = mid - 1
        else:
            return potentials[mid]


def test_sor_variable_omega(h):
    for omega_times_ten in range(10, 20):
        omega = float(omega_times_ten) / 10
        potential_matrix, num_iterations = sor(15, 0.08, 0.04, 0.2, h, omega)
        potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
        print "{}\t{}\t{}".format(omega, num_iterations, potential)


def test_sor_jacobi_variable_h(h):
    for x in xrange(5):
        potential_matrix, num_iterations = jacobi(15, 0.08, 0.04, 0.2, h)
        # potential_matrix, num_iterations = sor(15, 0.08, 0.04, 0.2, h, 1.3)
        potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
        print "{}\t{}\t{}\t{}".format(h, 1 / h, num_iterations, potential)
        h /= 2

if __name__ == '__main__':
    h = 0.02

    potential_matrix, num_iterations = sor(10, 0.08, 0.04, 0.2, h, 1.3)
    potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
    print potential

    # test_sor_variable_omega(h)
    # test_sor_jacobi_variable_h(h)

    A, initial_x, b, indices = setup_matrix_equation()

    # print_mat(A)
    # print_mat(b)

    # try:
    #     print "Solving Ax=b using Cholesky decomposition"
    #     x_chol = solve(A, b)
    #     print_mat(x_chol)
    # except Exception as e:
    #     print "Cholesky failed. Please make sure A is positive definite"

    A_transpose = transpose(A)
    A_pos_def = mult(A_transpose, A)
    b_new = mult(A_transpose, b)

    # print_mat(A_pos_def)
    # print_mat(b_new)

    ## Comment out cholesky while doing cg because cholesky modifies the b vector
    # x_chol = solve(A_pos_def, b_new)
    # print_mat(x_chol)
    # print(x_chol[11])

    x_cg, norm_2, norm_inf = cg(A_pos_def, b_new, initial_x)
    print get_potential_at_node(x_cg, indices, 19)
    # print_mat(x_cg)
    # print(x_cg[11])
    #
    # print "2-Norm"
    # for e in norm_2:
    #     print e
    # print "Infinity Norm"
    # for e in norm_inf:
    #     print e
