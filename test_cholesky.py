import random
from util import transpose
from util import vector_to_diag_matrix
from util import mult
from pprint import pprint

def generate_sym_pos_def_matrix(n, max):
    random_pos_matrix = [[float('%.2f'%(random.random()*max)) for i in range(n)] for i in range(n)]
    random_pos_matrix_transpose = transpose(random_pos_matrix)
    random_diagonal_matrix_vector = [[float('%.2f'%(random.random()*max))] for i in range(n)]
    random_diagonal_matrix = vector_to_diag_matrix(random_diagonal_matrix_vector)
    result = mult(mult(random_pos_matrix, random_diagonal_matrix), random_pos_matrix_transpose)

    pprint(random_pos_matrix)
    pprint(random_pos_matrix_transpose)
    pprint(random_diagonal_matrix_vector)
    pprint(random_diagonal_matrix)
    pprint(result)

if __name__ == '__main__':
    matrix = generate_sym_pos_def_matrix(3, 10)