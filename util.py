def transpose(A):
    return [list(x) for x in zip(*A)]

def mult(A, B):
    result = [[0 for x in xrange(len(B[0]))] for x in xrange(len(A))]
    for i in xrange(len(A)):
       for j in xrange(len(B[0])):
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    return result

def equal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    else:
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if A[i][j] != B[i][j]:
                    return False
    return True

def vector_to_diag_matrix(vector):
    diag = [[e for e in innerlist] for innerlist in vector]
    for idx, val in enumerate(diag): # Make y diagonal
        for i in xrange(len(diag)-1-idx):
            val.append(0)
        for i in xrange(idx):
            val.insert(0, 0)
    return diag
