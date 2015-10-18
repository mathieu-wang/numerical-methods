from util import print_mat


def sor(v_inner, w_inner, h_inner, length_outer, h, omega):

    size_of_mesh_matrix = int(length_outer/h) + 1
    mesh_matrix = [[0 for x in xrange(size_of_mesh_matrix)] for x in xrange(size_of_mesh_matrix)]

    inner_x_left = length_outer/2 - w_inner/2
    inner_x_left_node_index = int(inner_x_left / h)
    inner_x_right = inner_x_left + w_inner
    inner_x_right_node_index = int(inner_x_right / h)
    inner_y_bottom = length_outer/2 - h_inner/2
    inner_y_bottom_node_index = int(inner_y_bottom / h)
    inner_y_top = inner_y_bottom + h_inner
    inner_y_top_node_index = int(inner_y_top / h)

    # print inner_x_left_node_index, inner_x_right_node_index, inner_y_bottom_node_index, inner_y_top_node_index

    # Set values for inner conductor:
    for i in range(inner_x_left_node_index, inner_x_right_node_index+1):
        for j in range(inner_y_bottom_node_index, inner_y_top_node_index+1):
            mesh_matrix[i][j] = v_inner

    # print_mat(mesh_matrix)

    done = False
    num_iterations = 0
    while not done:
        done = True  # assume all residues are small enough. Change to false if at least one residue is too large

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    # Lower Left Quadrant:
                    mesh_matrix[i][j] = (1 - omega) * mesh_matrix[i][j] + omega / 4 * (mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1])
                    # Use symmetry to update the other 3 quadrants:
                    mesh_matrix[i][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]
                    mesh_matrix[size_of_mesh_matrix - i - 1][j] = mesh_matrix[i][j]
                    mesh_matrix[size_of_mesh_matrix - i - 1][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    residue = mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1] - 4*mesh_matrix[i][j]
                    # print residue
                    if abs(residue) >= 0.00001:
                        done = False
        num_iterations += 1
        # print(iterations)
    # print_mat(mesh_matrix)
    # print "Iterations:", num_iterations
    return mesh_matrix, num_iterations


def jacobi(v_inner, w_inner, h_inner, length_outer, h):
    size_of_mesh_matrix = int(length_outer / h) + 1
    mesh_matrix = [[0 for x in xrange(size_of_mesh_matrix)] for x in xrange(size_of_mesh_matrix)]
    # tmp_matrix = [[0 for x in xrange(size_of_mesh_matrix)] for x in xrange(size_of_mesh_matrix)]

    inner_x_left = length_outer / 2 - w_inner / 2
    inner_x_left_node_index = int(inner_x_left / h)
    inner_x_right = inner_x_left + w_inner
    inner_x_right_node_index = int(inner_x_right / h)
    inner_y_bottom = length_outer / 2 - h_inner / 2
    inner_y_bottom_node_index = int(inner_y_bottom / h)
    inner_y_top = inner_y_bottom + h_inner
    inner_y_top_node_index = int(inner_y_top / h)

    # print inner_x_left_node_index, inner_x_right_node_index, inner_y_bottom_node_index, inner_y_top_node_index

    # Set values for inner conductor:
    for i in range(inner_x_left_node_index, inner_x_right_node_index + 1):
        for j in range(inner_y_bottom_node_index, inner_y_top_node_index + 1):
            mesh_matrix[i][j] = v_inner

    # print_mat(mesh_matrix)

    done = False
    num_iterations = 0
    while not done:
        done = True  # assume all residues are small enough. Change to false if at least one residue is too large

        # Update tmp_matrix to be the previous mesh_matrix
        tmp_matrix = [x[:] for x in mesh_matrix]
        # print "tmp:"
        # print_mat(tmp_matrix)
        # print "mesh:"
        # print_mat(mesh_matrix)

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    # Lower Left Quadrant:
                    mesh_matrix[i][j] = (tmp_matrix[i - 1][j] + tmp_matrix[i][j - 1] + tmp_matrix[i + 1][j] + tmp_matrix[i][j + 1])/4.0

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                # Update tmp_matrix and use symmetry to update the other 3 quadrants:
                mesh_matrix[i][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i - 1][j] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i - 1][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]

                tmp_matrix[i][j] = mesh_matrix[i][j]
                tmp_matrix[i][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]
                tmp_matrix[size_of_mesh_matrix - i - 1][j] = mesh_matrix[i][j]
                tmp_matrix[size_of_mesh_matrix - i - 1][size_of_mesh_matrix - j - 1] = mesh_matrix[i][j]

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    residue = mesh_matrix[i - 1][j] + mesh_matrix[i][j - 1] + mesh_matrix[i + 1][j] + mesh_matrix[i][j + 1] - 4.0 * mesh_matrix[i][j]
                    # print residue
                    if abs(residue) >= 0.00001:
                        done = False
        num_iterations += 1
        # print(num_iterations)
        # print_mat(mesh_matrix)
    # print "Iterations:", num_iterations
    return mesh_matrix, num_iterations


def find_potential_at_point(potential_matrix, x_coord, y_coord):
    node_x = int(x_coord / h)
    node_y = int(y_coord / h)
    return potential_matrix[node_x][node_y]

if __name__ == '__main__':
    h = 0.01
    # for omega_times_ten in range(10, 20):
    #     omega = float(omega_times_ten) / 10
    #     potential_matrix, num_iterations = sor(15, 0.08, 0.04, 0.2, h, omega)
    #     potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
    #     print omega, num_iterations, potential

    h = 0.02
    for x in xrange(5):
        potential_matrix, num_iterations = jacobi(15, 0.08, 0.04, 0.2, h)
        potential = find_potential_at_point(potential_matrix, 0.06, 0.04)
        print h, 1/h, num_iterations, potential
        h /= 2