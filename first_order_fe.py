from util import cross
from util import dot
from util import print_mat
from util import subtract
from util import transpose
from util import mult


def edge(nodes, i):
    """
    Get the opposite edge vector of node at index i

    :param nodes: nodes in 2D Cartesian coordinates
    :param i: index of a node
    :return: opposite edge of i
    """
    len_nodes = len(nodes);
    prev_i = i - 1 if i > 0 else i - 1 + len_nodes
    next_i = (i + 1) % len_nodes
    return subtract(nodes[prev_i], nodes[next_i])


def get_local_s_matrix(nodes):
    len_nodes = len(nodes)
    S = [[0 for x in xrange(len_nodes)] for x in xrange(len_nodes)]
    for i in xrange(len_nodes):
        for j in xrange(len_nodes):
            edge_i = edge(nodes, i)
            edge_j = edge(nodes, j)
            dot_product = dot(edge_i, edge_j)
            area = area_of_triangle(nodes)
            S[i][j] = dot_product/(4*area)
    return S


def get_global_s_matrix(nodes1, nodes2):
    S1 = get_local_s_matrix(nodes_1)
    S2 = get_local_s_matrix(nodes_2)
    len_nodes = len(nodes_1)
    Sdis = [[0 for x in xrange(2*len_nodes)] for x in xrange(2*len_nodes)]
    for i in xrange(len_nodes):
        for j in xrange(len_nodes):
            Sdis[i][j] = S1[i][j]
            Sdis[i+len_nodes][j+len_nodes] = S2[i][j]
    C = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1],
         [1, 0, 0, 0],
         [0, 0, 1, 0]]

    C_transpose = transpose(C)
    S = mult(mult(C_transpose, Sdis), C)

    return S


def get_capacitance(W):
    # W = 0.5 * C * V^2
    V = 10
    C = 2*W/(V*V)
    return C


def get_total_energy(elements, coordinates, potentials):
    total_energy = 0
    for element in elements:
        energy = get_element_energy(element, coordinates, potentials)
        total_energy += energy
    return total_energy*4 # symmetry


def get_element_energy(node_indices, coordinates, potentials):
    epsilon0 = 8.854187817 * pow(10, -12)
    nodes = []
    U = []
    for node_index in node_indices:
        node_coords = coordinates[node_index]
        nodes.append(node_coords)
        U.append(potentials[node_index])
    S = get_local_s_matrix(nodes)
    U_transpose = transpose(U)
    first_mult = mult(U_transpose, S)
    W = 0.5 * epsilon0 * mult(first_mult, U)[0][0] # convert 1x1 matrix to scalar value
    return W


def area_of_triangle(nodes):
    edge2 = edge(nodes, 1)
    edge3 = edge(nodes, 2)
    return 0.5*cross(edge2, edge3)


def read_potentials(filename):
    potentials = [[-1.0]]
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        splitted_line = line.split()

        if splitted_line:
            potentials.append([float(splitted_line[3])])
    return potentials


def read_coordinates(filename):
    coordinates = [[-1, -1]]
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines[:34]:
        splitted_line = line.split()

        if splitted_line:
            coordinates.append([float(splitted_line[1]), float(splitted_line[2])])
    return coordinates


def read_elements(filename):
    elements = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines[35:81]:
        splitted_line = line.split()

        if splitted_line:
            elements.append([int(splitted_line[0]), int(splitted_line[1]), int(splitted_line[2])])
    return elements

if __name__ == '__main__':
    nodes_1 = [[0.00, 0.02],
               [0.00, 0.00],
               [0.02, 0.00]]

    nodes_2 = [[0.02, 0.02],
               [0.00, 0.02],
               [0.02, 0.00]]

    # print(edge(nodes_1, 0))
    # print(edge(nodes_1, 1))
    # print(edge(nodes_1, 2))

    # print dot(edge(nodes_1, 0), edge(nodes_1, 1))

    S1 = get_local_s_matrix(nodes_1)
    print "Local S matrix for element 1:"
    print_mat(S1)
    print "Local S matrix for element 2:"
    S2 = get_local_s_matrix(nodes_2)
    print_mat(S2)
    print "Global S matrix for elements 1 and 2:"
    S = get_global_s_matrix(nodes_1, nodes_2)
    print_mat(S)

    elements = read_elements('data.txt')
    coordinates = read_coordinates('data.txt')
    potentials = read_potentials('potentials.txt')

    W = get_total_energy(elements, coordinates, potentials)
    print "Total Energy:", W/(pow(10, -9)), "nJ"
    print "Capacitance per unit length:", get_capacitance(W)/(pow(10, -12)), "pF"
