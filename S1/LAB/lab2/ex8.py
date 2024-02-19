import numpy as np

def mat_trace(matrix):
    try:
        # Check if the matrix is square
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Error: The input matrix is not square.")
        
        # Calculate the trace of the matrix
        trace = np.trace(matrix)
        return trace
    except ValueError as e:
        print(e)
        return None

# Example usage:
square_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

trace_result = mat_trace(square_matrix)

if trace_result is not None:
    print("Matrix Trace:", trace_result)
