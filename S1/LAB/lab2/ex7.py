import numpy as np

def mat_prod(mat1, mat2):
    try:
        result = np.dot(mat1, mat2)
        return result
    except ValueError:
        # Matrices are not compatible for multiplication
        print("Error: Matrices are not compatible for multiplication.")
        return np.array([])

# Example usage:
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result_matrix = mat_prod(matrix1, matrix2)

if result_matrix.size > 0:
    print("Matrix Product:")
    print(result_matrix)
else:
    print("Matrix multiplication is not possible.")