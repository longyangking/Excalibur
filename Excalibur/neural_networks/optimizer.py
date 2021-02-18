import numpy as np
from .loss_function import *

class Optimizer:
    def __init__(self, network, name="SGD", loss_function="MSE"):
        self.network = network
        self.name = name
        if name not in ["SGD", "Adam"]:
            raise Exception("Not found: Unsupported optimizer for neural network!")

        if loss_function not in ["ABS", "MSE", "cross_entropy"]:
            raise Exception("Not found: Unsupported loss function for neural network!")

        self.loss_function = MSE

        if loss_function == "ABS":
            self.loss_function = ABS
        elif loss_function == "cross_entropy":
            self.loss_function = cross_entropy
        
    def optimize(self, x, y, learning_rate):
        layers = self.network.get_layers()

        if self.name == "SGD":
            values = [x]
            for layer in layers:
                values.append(layer.get_value(values[-1]))
            error = self.loss_function(values[-1], y)

            # Back-propagation of error
            deltas = [error*layers[-1].activation_deriv_function(values[-1])]
            for index in range(len(values)-2,0,-1):
                deltas.append(\
                    deltas[-1].dot(layers[index].get_weight.T)*layers[index].activation_deriv_function(values[index]))
            deltas.reverse()    # The first element of original set should belong to the last one. 

            # Update Weights
            for i in range(len(layers)):
                value = np.atleast_2d(values[i])
                delta = np.atleast_2d(deltas[i])
                layers[i].update_weight(learning_rate*value.T.dot(delta))
