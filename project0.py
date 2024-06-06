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

