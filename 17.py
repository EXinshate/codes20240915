import numpy.linalg
import numpy as np

#矩阵与线性代数运算
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
#print(numpy.linalg.det(m))

#print(numpy.linalg.eigvals(m))
v = np.matrix([[2], [3],[4]])
x = numpy.linalg.solve(m, v)
#print(x)
#print(m*x)
print(v)