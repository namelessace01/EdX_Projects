import numpy as np

# Write a function called randomization that takes as input a positive integer n, and returns A, a random n x 1 Numpy array.
def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.random.random([n, 1])


# Write a function called operations that takes as input two positive integers h and w, 
# makes two random matrices A and B, of size h x w, and returns A,B, and s, the sum of A and B.

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
    A = np.random.random([h, w])
    B = np.random.random([h, w])
    s = A + B
    
    return A, B, s


# Write a function called norm that takes as input two Numpy column arrays A and B, 
# adds them, and returns s, the L2 norm of their sum.

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    c = A + B
    s = np.linalg.norm(c)
    
    return s


# Here, we will write a function neural_network, which will apply a neural network 
# operation with 2 inputs and 1 output and a given weight matrix.
# Your function should take two arguments: inputs and weights, two NumPy arrays of shape  
# (2, 1) and should return a NumPy array of shape (1, 1), the output of the neural network. 
# Do not forget the tanh activation.

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    inputs = np.array(inputs)
    weights = np.array(weights)

    z = np.dot(inputs.T, weights)
    output = np.tanh(z)
    
    return output


# Let's start with writing a scalar function scalar_function, which will apply the following 
# operation with input x and y.
# f(x, y) = {"""x * y (if x <= y)
#               else x / y"""}
# Note that x and y are scalars.

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    return x * y if x <= y else x / y