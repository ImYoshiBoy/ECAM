import numpy as np

def in_mat(element, matrix):
    try:
        # Convert the matrix to a NumPy array if it is not already
        matrix = np.array(matrix)
        
        # Check if the element is present in the matrix
        result = np.any(matrix == element)
        return result
    except ValueError as e:
        print(e)
        return False

# Example usage:
matrix_to_check = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
element_to_find = 5

if in_mat(element_to_find, matrix_to_check):
    print(f"{element_to_find} is in the matrix.")
else:
    print(f"{element_to_find} is not in the matrix.")
