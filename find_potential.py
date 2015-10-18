from util import print_mat

def sor(v_inner, w_inner, h_inner, length_outer, h, omega):

    size_of_mesh_matrix = int(length_outer/h) + 1
    mesh_matrix = [[0 for x in xrange(size_of_mesh_matrix)] for x in xrange(size_of_mesh_matrix)]

    print_mat(mesh_matrix)

    inner_x_left = length_outer/2 - w_inner/2
    inner_x_left_node_index = int(inner_x_left / h)
    inner_x_right = inner_x_left + w_inner
    inner_x_right_node_index = int(inner_x_right / h)
    inner_y_bottom = length_outer/2 - h_inner/2
    inner_y_bottom_node_index = int(inner_y_bottom / h)
    inner_y_top = inner_y_bottom + h_inner
    inner_y_top_node_index = int(inner_y_top / h)

    print inner_x_left_node_index, inner_x_right_node_index, inner_y_bottom_node_index, inner_y_top_node_index

    # Set values for inner conductor:
    for i in range(inner_x_left_node_index, inner_x_right_node_index+1):
        for j in range(inner_y_bottom_node_index, inner_y_top_node_index+1):
            mesh_matrix[i][j] = v_inner

    # print_mat(mesh_matrix)

    done = False
    num_iterations = 0
    while not done:
        done = True # assume all residues are small enough. Change to false if at least one residue is too large

        # Update lower-left quadrant
        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    mesh_matrix[i][j] = (1 - omega) * mesh_matrix[i][j] + omega / 4 * (mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1])

        # Update other quadrants
        for i in range(1, (size_of_mesh_matrix / 2)):
            for j in range(1, (size_of_mesh_matrix / 2)):
                mesh_matrix[i][size_of_mesh_matrix-j-1] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i-1][j] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i-1][size_of_mesh_matrix-j-1] = mesh_matrix[i][j]

        # print_mat(mesh_matrix)

        for i in range(1, (size_of_mesh_matrix / 2) + 1):
            for j in range(1, (size_of_mesh_matrix / 2) + 1):
                if not (inner_x_left_node_index <= i <= inner_x_right_node_index and inner_y_bottom_node_index <= j <= inner_y_top_node_index):
                    residue = mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1] - 4*mesh_matrix[i][j]
                    print residue
                    if abs(residue) >= 0.00001:
                        done = False
                        break
            if not done:
                break
        num_iterations += 1
        # print(iterations)
    print_mat(mesh_matrix)
    print(num_iterations)
    return mesh_matrix


if __name__ == '__main__':
    h = 0.02
    potential_matrix = sor(15, 0.08, 0.04, 0.2, h, 1.0)
    node_x = int(0.06 / h)
    node_y = int(0.04 / h)
    print node_x
    print node_y
    print potential_matrix[node_x][node_y]
