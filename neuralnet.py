# A standard feed-forward neural network

# Inputs - grid (size: height x width) of game state where 0 = null, 1 = snakehead, 2 = snake, 3 = apple
# Outputs - array of four values representing up, down, right, left

import numpy as np
from math import e

class NeuralNet:

    def __init__(self, grid):
        self.inputs = np.zeros(10000)
        self.outputs = np.zeros(4)
        self.weights1 = np.random.random_sample(10000,16)
        self.weights2 = np.random.random_sample(16, 16)
        self.weights3 = np.random.random_sample(16,4)

        def firstLayerNeurons(self):
            self.firstLayerNeurons  = relu(np.dot(self.inputs, self.weights1))
            return self.firstLayerNeurons

        def secondLayerNeuron(self):
            self.secondLayerNeurons = relu(np.dot(self.firstLayerNeurons, self.weights2))

        def outputNerons(self):
            self.outputs = relu(np.dot(self.secondLayerNeurons, self.weights3))

        def relu(value):
            x,y = np.shape(value)
            for row in x:
                for column in y:
                    value = max(0, value)
            return value


# class HiddenLayer:
#
#     def __init__(self, neuronsPerLayer):
#         self.neurons = []
#
#         for neuron in range(0, neuronsPerLayer):
#             self.neurons.append(Neuron('RELU'))
#
#
# class Neuron:
#
#     def __init__(self, activationFunction):
#         self.activationFunction = activationFunction
#         self.value = 0
#
#     def activate(self, computedValue):
#         if self.activationFunction == 'RELU':
#             neuronValue = relu(computedValue)
#         if self.activationFunction == 'SIGMOID':
#             neuronValue = sigmoid(com[computedValue])
#         return neuronValue
#
#     def relu(self, computedValue):
#         neuronValue = max(0,computedValue)
#         return neuronValue
#
#     def sigmoid(self, computedValue):
#         neuronValue = (math.e^computedValue)/(math.e^computedValue + 1)
#         return neuronValue
