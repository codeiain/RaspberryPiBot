from NN.NeuralNetwork import NeuralNetwork

nn = NeuralNetwork()
print nn
#help(NeuralNetwork)
nn.add_layer(2, 2)
nn.add_layer(2, 2)
nn.add_layer(2, 2)
readings = [0,0,1]
expected = [1,0,0]

nn.train_network(readings, expected)