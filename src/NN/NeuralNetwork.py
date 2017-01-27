import Layer
import random

class NeuralNetwork:
    @classmethod
    def __init__(self):
        """
        the default learning rate of a neural network is set to 0.1, which can changed by the setLearningRate(lR) function.
        """
        self.layers = []
        self.array_of_inputs = []
        self.array_of_outputs = []
        self.learning_rate = 0.1
        self.network_error = 0
        self.training_error = 0
        self.retrain_chances=0

    @classmethod
    def add_layer(self, num_connections, num_neurons):
        """
        Function to add a Layer to the Neural Network
        :param num_connections:
        :param num_neurons:
        :return:
        """
        self.layers.append(Layer.Layer(num_connections, num_neurons))

    @classmethod
    def get_layer_count(self):
        """
        unction to return the number of layers in the neural network
        :return:
        """
        return len(self.layers)

    @classmethod
    def set_learning_rate(self, temp_learning_rate):
        """
        Function to set the learningRate of the Neural Network
        :param temp_learning_rate:
        :return:
        """
        self.learning_rate = temp_learning_rate

    @classmethod
    def set_inputs(self, temp_inputs):
        """
        Function to set the inputs of the neural network
        :param temp_inputs:
        :return:
        """
        self.array_of_inputs = temp_inputs

    @classmethod
    def set_layer_inputs(self,temp_inputs, layer_index):
        """
        Function to set the inputs of a specified layer
        :param temp_inputs:
        :param layer_index:
        :return:
        """
        if layer_index > self.get_layer_count() -1:
            print "NN Error: setLayerInputs: layerIndex=" + layer_index + " exceeded limits= " + str(self.get_layer_count() -1)
        else:
            self.layers[layer_index].set_inputs(temp_inputs)

    @classmethod
    def set_outputs(self, temp_outputs):
        """
        Function to set the outputs of the neural network
        :param temp_outputs:
        :return:
        """
        self.array_of_outputs = temp_outputs

    @classmethod
    def get_outputs(self):
        """
        Function to return the outputs of the Neural Network
        :return:
        """
        return self.array_of_outputs

    @classmethod
    def process_inputs_to_outputs(self, temp_inputs):
        """
        Function to process the Neural Network's input values and convert them to an output pattern using ALL layers in the network
        :param temp_inputs:
        :return:
        """
        self.set_inputs(temp_inputs)
        if self.get_layer_count > 0:
            if len(self.array_of_inputs) != self.layers[0].neurons[0].get_connection_count():
                print "NN Error: processInputsToOutputs: The number of inputs do NOT match the NN"
                exit()
            else:
                for i in range(0 , self.get_layer_count()):
                    if i ==0:
                        self.set_layer_inputs(self.array_of_inputs,i)
                    else:
                        self.set_layer_inputs(self.layers[i-1].actual_output, i)

                    self.layers[i].process_inputs_to_outputs()

                self.set_outputs(self.layers[self.get_layer_count()-1].actual_output)
        else:
            print "Error: There are no layers in this Neural Network"
            exit()

    @classmethod
    def train_network(self, input_data, expected_output_data):
        """
        Function to train the entire network using an array.
        :param input_data:
        :param expected_output_data:
        :return:
        """
        self.process_inputs_to_outputs(input_data)
        for i in range(self.get_layer_count() -1, 0, -1):
            if i == self.get_layer_count() -1:
                self.layers[i].set_delta_error(expected_output_data)
                self.layers[i].train_layer(self.learning_rate)
                self.network_error = self.layers[i].get_layer_error()
            else:
                for j in range(0, self.layers[i].get_neuron_count()):
                    self.layers[i].neurons[j].delta_error = 0
                    for k in range(0, self.layers[i+1].get_neuron_count()):
                        self.layers[i].neurons[j].delta_error += (self.layers[i+1].neurons[k].connections[j].weight * self.layers[i+1].neurons[k].detla_error)

                    self.layers[i].neurons[j].delta_error = (self.layers[i].neurons[j].neuron_output_value * (1-self.layers[i].neurons[j].neuron_output_value))
                self.layers[i].train_layer(self.learning_rate)
                self.layers[i].clear_expected_output()

    @classmethod
    def training_cycle(self, training_input_data, training_expected_data, train_randomly):
        """
        Function to train the entire network, using an array of input and expected data within an ArrayList
        :param training_input_data:
        :param training_expected_data:
        :param train_randomly:
        :return:
        """
        dataindex = 0
        training_error = 0
        for i in range(0, len(training_input_data)):
            if train_randomly:
                dataindex = random(0, len(training_input_data))
            else:
                dataindex = i

            self.train_network((training_input_data[i], training_expected_data[i],))
            training_error += abs(self.network_error)

    @classmethod
    def auto_train_network(self, training_input_data, training_expected_data, training_error_target, cycle_limit):
        """
        Function to train the network until the Error is below a specific threshold
        :param training_input_data:
        :param training_expected_data:
        :param training_error_target:
        :param cycle_limit:
        :return:
        """
        training_error = 9999
        training_counter = 0

        while training_error > training_error_target and training_counter < cycle_limit:
            training_error = 0
            self.training_cycle(training_input_data, training_expected_data, True)
            training_counter=+1

        if training_counter < cycle_limit:
            self.training_cycle(training_input_data,training_expected_data, False)
            training_counter=+1

            if training_error > training_error_target:
                if self.retrain_chances < 10:
                    self.retrain_chances =+1
                    self.auto_train_network(training_input_data, training_expected_data, training_error_target, cycle_limit)
        else:
            print "CycleLimit has been reached. Has been retrained " + self.retrain_chances + " times.  Error is = " +self.training_error

