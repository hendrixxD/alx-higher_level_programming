matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[1, 2, 3],[4, 5, 6]]
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, 12))
print(matrix_divided(matrix, -2))
print(matrix_divided(matrix, [1,2]))
print(matrix_divided(matrix, {2,3}))
matrix = [[2,3,4,6],[5,3,6,2]]
print(matrix)
print(matrix_divided(matrix, float('NaN')))
print(matrix_divided(matrix, float('inf')))
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, -6))
matrix = [[-2,-33,4,6],[-5,3,-6,2]]
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, 4))
print(matrix_divided(matrix, -333))
