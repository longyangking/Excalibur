import numpy as np
from .activation_function import *

class DenseLayer:
    def __init__(self, numbers, activation='tanh', name=None, initial_weight=None):
        self.name = name
        self.numbers = numbers
        
        self.activation = tanh
        self.activation_deriv = tanh_deriv

        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_deriv
        elif activation == 'relu':
            self.activation = relu
            self.activation_deriv = relu_deriv

        number1, number2 = numbers
        if initial_weight is None:
            self.weight = (2*np.random.random((number1+1, number2+1))-1)*0.25 
            # extra "+1" means the bias
        else:
            self.weight = initial_weight

    def get_value(self, value):
        return self.activation(np.dot(value, self.weight))

    def get_numbers(self):
        return self.numbers  

    def get_weight(self):
        return self.weight

    def update_weight(self, weight):
        self.weight += weight

    def activation_function(self, value):
        return self.activation(value)

    def activation_deriv_function(self, value):
        return self.activation_deriv(value)