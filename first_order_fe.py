from util import cross
from util import dot
from util import print_mat
from util import subtract
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

def area_of_triangle(nodes):
    edge2 = edge(nodes, 1)
    edge3 = edge(nodes, 2)
    return 0.5*cross(edge2, edge3)

if __name__ == '__main__':
    nodes = [[0.00, 0.02],
             [0.00, 0.00],
             [0.02, 0.00]]

    print(edge(nodes, 0))
    print(edge(nodes, 1))
    print(edge(nodes, 2))

    print dot(edge(nodes, 0), edge(nodes, 1))

    print area_of_triangle(nodes)

    S = get_local_s_matrix(nodes)
    print_mat(S)