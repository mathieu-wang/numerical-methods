import random
from util import transpose
from util import vector_to_diag_matrix
from util import mult
from util import det
from util import equal
from util import print_mat
from cholesky import solve
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
        matrix = generate_sym_pos_def_matrix(5, 2)
        print("matrix:")
        print_mat(matrix)
        print("det(matrix):")
        print(det(matrix))
        self.assertTrue(equal(matrix, transpose(matrix)))
        self.assertTrue(det(matrix) > 0)

    def print_cholesky_results(self, A, x):
        print("A:")
        print_mat(A)
        print("det(A):")
        print(det(A))
        print("x:")
        print_mat(x)
        print("b = mult(A, x):")
        b = mult(A, x)
        print_mat(b)
        print("solved x:")
        print_mat(solve(A, b))

    def test_cholesky_2x2(self):
        A = generate_sym_pos_def_matrix(2, 2)
        x = [[1.5], [-2.0]]
        self.print_cholesky_results(A, x)

    def test_cholesky_3x3(self):
        A = generate_sym_pos_def_matrix(3, 2)
        x = [[20], [-2], [0.2]]
        self.print_cholesky_results(A, x)

    def test_cholesky_4x4(self):
        A = generate_sym_pos_def_matrix(4, 2)
        x = [[1], [3], [5], [7]]
        self.print_cholesky_results(A, x)

    def test_cholesky_5x5(self):
        A = generate_sym_pos_def_matrix(5, 2)
        x = [[-2], [-4], [-6], [-8], [-10]]
        self.print_cholesky_results(A, x)

if __name__ == '__main__':
    unittest.main()
