import numpy as np
from .layer import DenseLayer
from .optimizer import Optimizer

class NeuralNetwork:
    def __init__(self, input_dim, output_dim, layer_info):
        self.layer_info = layer_info

        numbers = [input_dim]
        activation_funcs = list()
        for info in layer_info:
            number, activation_func = info
            numbers.append(number)
            activation_funcs.append(activation_func)
        numbers.append[output_dim]

        layers = list()
        for i in range(1, len(numbers)+1):
            layer = DenseLayer(
                [numbers[i-1], numbers[i]], 
                activation=activation_func[i-1]
            )
            layers.append(layer)

        self.network = Network(layers)

    def fit(self, X, y, verbose=False):
        self.network.fit(X, y)

    def predict(self, x):
        return self.predict(x)

class Network:
    def __init__(self,layers):
        self.layers = layers

    def get_layers(self):
        return self.layers

    def fit(self,X,y,optimzer="SGD",learning_rate=0.2,epochs=10000):
        X = np.atleast_2d(X) 
        temp = np.ones([X.shape[0],X.shape[1]+1])
        temp[:,0:-1] = X   
        X = temp
        y = np.array(y) 

        optimizer = Optimizer(self)

        for k in range(epochs):
            index = np.random.randint(X.shape[0])
            optimizer.optimize(X[index], y[index], learning_rate=learning_rate)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x  # Add bias term
        pred = temp
        for layer in self.network.get_layers():
            pred = layer.get_value(pred)
        return pred