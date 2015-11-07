from util import subtract
from util import add
from util import mult
from util import scalar_mult
from util import transpose
from util import norm


def cg(A, b, x0):
    error = 0.00001
    x = x0
    r0 = subtract(b, mult(A, x))
    p = r0
    i = 0
    norm_2 = []
    norm_inf = []
    while True:
        r0_transpose = transpose(r0)
        p_transpose = transpose(p)
        num = mult(r0_transpose, r0)[0][0]
        denom = mult(mult(p_transpose, A), p)[0][0]
        alpha = float(num) / float(denom)
        x = add(x, scalar_mult(p, alpha))
        alphaA = scalar_mult(A, alpha)
        alphaAp = mult(alphaA, p)
        ri = subtract(r0, alphaAp)

        ri_norm = norm(ri, 1)
        print i, ri_norm
        norm_2.append(norm(ri, 2))
        norm_inf.append(norm(ri, 'inf'))

        if ri_norm < error:
            return x, norm_2, norm_inf
        ri_transpose = transpose(ri)
        num = mult(ri_transpose, ri)[0][0]
        denom = mult(r0_transpose, r0)[0][0]
        beta = float(num) / float(denom)
        p = add(ri, scalar_mult(p, beta))
        r0 = ri
        i += 1
    return x


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

    # Set values for inner conductor:
    for i in range(inner_x_left_node_index, inner_x_right_node_index+1):
        for j in range(inner_y_bottom_node_index, inner_y_top_node_index+1):
            mesh_matrix[i][j] = v_inner

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