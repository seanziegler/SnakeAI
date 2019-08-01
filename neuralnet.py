# A standard feed-forward neural network

# Inputs - grid (size: height x width) of game state where 0 = null, 1 = snakehead, 2 = snake, 3 = apple
# Outputs - array of four values representing up, down, right, left

import numpy as np
from math import e

class NeuralNet:

    def __init__(self):
        self.inputs = np.zeros(30000)
        self.outputs = np.zeros(4)
        self.hiddenLayers = 2
        self.neuronsPerLayer = 16


class Neuron:

    def __init__(self, activationFunction):
        self.activationFunction = activationFunction
        self.value = 0

    def activate(self, activationValue):
        if self.activationFunction == 'RELU':
            relu(activationValue)
        return activationValue

    def relu(self, computedValue):
        activationValue = max(0,computedValue)
        return activationValue

    def sigmoid(self, computedValue):
        activationValue = (e^computedValue)/(e^computedValue + 1)
        return activationValue

class Layer:

    def __init__(self):
        layer = []

        for neuron in self.neuronsPerLayer:
            layer.append(Neuron('RELU'))
