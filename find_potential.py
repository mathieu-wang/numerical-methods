from util import print_mat

def sor(v_inner, v_outer, w_inner, h_inner, length_outer, h, omega):

    size_of_mesh_matrix = int(length_outer/h) + 1
    mesh_matrix = [[0 for x in xrange(size_of_mesh_matrix+1)] for x in xrange(size_of_mesh_matrix+1)]

    # print_mat(mesh_matrix)

    inner_x_left = (length_outer - w_inner) / 2
    inner_x_right = inner_x_left + w_inner
    inner_y_bottom = (length_outer - h_inner) / 2
    inner_y_top = inner_y_bottom + h_inner

    inner_x_left_node = int(inner_x_left / h) + 1
    inner_x_right_node = int(inner_x_right / h) + 1
    inner_y_bottom_node = int(inner_y_bottom / h) + 1
    inner_y_top_node = int(inner_y_top / h) + 1

    for i in range(inner_x_left_node, inner_x_right_node+1):
        for j in range(inner_y_bottom_node, inner_y_top_node+1):
            mesh_matrix[i][j] = v_inner

    for i in range(1, size_of_mesh_matrix):
        mesh_matrix[i][1] = v_outer
        mesh_matrix[i][size_of_mesh_matrix] = v_outer
        mesh_matrix[1][i] = v_outer
        mesh_matrix[size_of_mesh_matrix][i] = v_outer

    # del mesh_matrix[0]
    # for row in mesh_matrix:
    #     del row[0]
    # print_mat(mesh_matrix)

    done = False
    iterations = 0
    while not done:
        done = True
        for i in range(2, (size_of_mesh_matrix / 2) + 2):
            for j in range(2, (size_of_mesh_matrix / 2) + 2):
                if not (i >= inner_x_left_node and i <= inner_x_right_node and j >= inner_y_bottom_node and j <= inner_y_top_node):
                    mesh_matrix[i][j] = (1 - omega) * mesh_matrix[i][j] + omega / 4 * (mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1])

        for i in range(2, (size_of_mesh_matrix / 2) + 2):
            for j in range (2, (size_of_mesh_matrix / 2) + 2):
                mesh_matrix[i][size_of_mesh_matrix-j+1] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i + 1][j] = mesh_matrix[i][j]
                mesh_matrix[size_of_mesh_matrix - i + 1][size_of_mesh_matrix-j+1] = mesh_matrix[i][j]

        # print_mat(mesh_matrix)

        for i in range(2, (size_of_mesh_matrix / 2) + 2):
            for j in range(2, (size_of_mesh_matrix / 2) + 1):
                if not (i >= inner_x_left_node and i <= inner_x_right_node and j >= inner_y_bottom_node and j <= inner_y_top_node):
                    residue = mesh_matrix[i-1][j] + mesh_matrix[i][j-1] + mesh_matrix[i+1][j] + mesh_matrix[i][j+1] - 4*mesh_matrix[i][j]
                    print residue
                    if abs(residue) >= 0.00001:
                        # print "set to false"
                        done = False
                        break
            if not done:
                break
        iterations += 1
        # print(iterations)
    print_mat(mesh_matrix)
    print(iterations)
    return mesh_matrix


if __name__ == '__main__':
    h = 0.02
    potential_matrix = sor(15, 0, 0.08, 0.04, 0.2, h, 1.3)
    node_x = int(0.06 / h)
    node_y = int(0.04 / h)
    print node_x
    print node_y
    print potential_matrix[node_x][node_y]
