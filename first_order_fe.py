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

def get_local_s_matrix():
    pass

if __name__ == '__main__':
    nodes = [[0.00, 0.02],
             [0.00, 0.00],
             [0.02, 0.00]]

    print(edge(nodes, 0))
    print(edge(nodes, 1))
    print(edge(nodes, 2))

    print dot(edge(nodes, 0), edge(nodes, 1))