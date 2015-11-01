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


def area_of_triangle(nodes):
    edge2 = edge(nodes, 1)
    edge3 = edge(nodes, 2)
    return 0.5*cross(edge2, edge3)


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

    # print area_of_triangle(nodes_1)

    S1 = get_local_s_matrix(nodes_1)
    print_mat(S1)
    print ""
    S2 = get_local_s_matrix(nodes_2)
    print_mat(S2)
    print ""
    S = get_global_s_matrix(nodes_1, nodes_2)
    print_mat(S)