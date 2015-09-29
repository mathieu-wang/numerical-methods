def transpose(A):
    return [list(x) for x in zip(*A)]

def mult(A, B):
    print "test mult"
    print len(A)
    print len(A[0])
    print len(B)
    print len(B[0])
    result = [[0 for x in xrange(len(B[0]))] for x in xrange(len(A))]
    from pprint import pprint
    pprint(result)
    for i in xrange(len(A)):
       for j in xrange(len(B[0])):
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    return result