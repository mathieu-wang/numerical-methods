from finite_difference_methods import sor
from finite_difference_methods import jacobi


def find_potential_at_point(potential_matrix, x_coord, y_coord):
    node_x = int(x_coord / h)
    node_y = int(y_coord / h)
    return potential_matrix[node_x][node_y]


def setup_matrix_equation():
    A = [[-4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, -4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

    # test_sor_variable_omega(h)
    # test_sor_jacobi_variable_h(h)

