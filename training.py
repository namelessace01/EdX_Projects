# import numpy as np
# x = [1, 5]
# x = np.array(x)
# print(x)
#
# y = [[3, 5, 7], [2, 4, 6]]
# y = np.array(y)
# print(f"The dimension of y is: {y.shape}")
#
# print(np.zeros([4, 5]))
# print(np.ones([5, 6]))
#
# print(np.random.random([4, 5]))
#
#
# def randomization(n):
#     """
#     Arg:
#       n - an integer
#     Returns:
#       A - a randomly-generated nx1 Numpy array.
#     """
#     # Your code here
#     A = np.random.random([n, 1])
#     return f"Randomization: {A}"
#
#
# print(randomization(6))
#
# a = [[1, 3, 5, 7], [2, 4, 6, 8]]
# a = np.array(a)
# print(f"The matrix a is: {a}")
# b = a.transpose()
# print(f"The transpose of matrix a is: {b}")
#
# print(f"Matrix multiplication: {np.matmul(x, a)}")
#
#
# def operations(h, w):
#     """
#     Takes two inputs, h and w, and makes two Numpy arrays A and B of size
#     h x w, and returns A, B, and s, the sum of A and B.
#
#     Arg:
#       h - an integer describing the height of A and B
#       w - an integer describing the width of A and B
#     Returns (in this order):
#       A - a randomly-generated h x w Numpy array.
#       B - a randomly-generated h x w Numpy array.
#       s - the sum of A and B.
#     """
#     # Your code here
#     A = np.random.random([h, w])
#     B = np.random.random([h, w])
#     s = A + B
#
#     return f"Random A: {A}, Random B: {B}, Sum s: {s}"
#
#
# print(operations(4, 5))
#
#
# def neural_network(inputs, weights):
#     """
#      Takes an input vector and runs it through a 1-layer neural network
#      with a given weight matrix and returns the output.
#
#      Arg:
#        inputs - 2 x 1 NumPy array
#        weights - 2 x 1 NumPy array
#      Returns (in this order):
#        out - a 1 x 1 NumPy array, representing the output of the neural network
#     """
#     # Your code here
#     inputs = np.array(inputs)
#     weights = np.array(weights)
#
#     z = np.dot(inputs.T, weights)
#     output = np.tanh(z)
#
#     return output
#
#
# print(neural_network([[0.64312635], [0.9049285]],
#                      [[0.9447287], [0.41797513]]))
#
#
# def scalar_function(x, y):
#     """
#     Returns the f(x,y) defined in the problem statement.
#     """
#     # Your code here
#     return x * y if x <= y else x / y
#
#
# print(scalar_function(3, 6))
#
#
# def vector_function(x, y):
#     """
#     Make sure vector_function can deal with vector input x,y
#     """
#     # Your code here
#     def scalar_function(a, b):
#         return a * b if a <= b else a / b
#
#     vectorized_scalar = np.vectorize(scalar_function)
#     return vectorized_scalar(x, y)
#
#
# print(vector_function(5, 9))
