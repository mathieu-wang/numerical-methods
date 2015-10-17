import random
from util import transpose
from util import vector_to_diag_matrix
from util import mult
from util import det
from util import equal
from util import print_mat
import unittest


def generate_sym_pos_def_matrix(n, max):
    random_pos_matrix = [[float('%.2f' % (random.random() * max)) for i in range(n)] for i in range(n)]
    random_pos_matrix_transpose = transpose(random_pos_matrix)
    random_diagonal_matrix_vector = [[float('%.2f' % (random.random() * max))] for i in range(n)]
    random_diagonal_matrix = vector_to_diag_matrix(random_diagonal_matrix_vector)
    result = mult(mult(random_pos_matrix, random_diagonal_matrix), random_pos_matrix_transpose)

    # pprint(random_pos_matrix)
    # pprint(random_pos_matrix_transpose)
    # pprint(random_diagonal_matrix_vector)
    # pprint(random_diagonal_matrix)
    # pprint(result)
    return result


class TestCholesky(unittest.TestCase):
    def setUp(self):
        print "In method", self._testMethodName

    def test_generate_sym_pos_def_matrix(self):
        matrix = generate_sym_pos_def_matrix(5, 5)
        print("matrix:")
        print_mat(matrix)
        print("det(matrix):")
        print(det(matrix))
        self.assertTrue(equal(matrix, transpose(matrix)))
        self.assertTrue(det(matrix) > 0)

    def test_cholesky_2x2(self):
        matrix = generate_sym_pos_def_matrix(2, 10)
        print("A:")
        print_mat(matrix)
        print("det(matrix):")
        print(det(matrix))


if __name__ == '__main__':
    unittest.main()
