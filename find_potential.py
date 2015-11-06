from finite_difference_methods import sor
from finite_difference_methods import jacobi


def find_potential_at_point(potential_matrix, x_coord, y_coord):
    node_x = int(x_coord / h)
    node_y = int(y_coord / h)
    return potential_matrix[node_x][node_y]

if __name__ == '__main__':
    h = 0.02

    for omega_times_ten in range(10, 20):
        omega = float(omega_times_ten) / 10
        potential_matrix, num_iterations = sor(15, 0.08, 0.04, 0.2, h, omega)
        potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
        print "{}\t{}\t{}".format(omega, num_iterations, potential)

    for x in xrange(5):
        potential_matrix, num_iterations = jacobi(15, 0.08, 0.04, 0.2, h)
        # potential_matrix, num_iterations = sor(15, 0.08, 0.04, 0.2, h, 1.3)
        potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
        print "{}\t{}\t{}\t{}".format(h, 1/h, num_iterations, potential)
        h /= 2