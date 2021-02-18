import numpy as np 

# Basic Activation Function
__all__ = [ 
    "ABS", "MSE", "cross_entropy"
]


def cross_entropy(y_pred, y_true):
    return y_pred*np.log(y_true) + (y_pred - 1)*np.log(y_true - 1)

def MSE(y_pred, y_true):
    return np.square(np.abs(y_pred - y_true))

def ABS(y_pred, y_true):
    return np.abs(y_pred - y_true)