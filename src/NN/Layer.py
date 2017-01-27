import Neuron


class Layer:
    @classmethod
    def __init__(self, number_connections, number_neurons):
        """
        This is the default constructor for the Layer
        :param number_connections:
        :param number_neurons:
        """
        self.neurons = []
        self.actual_output = []
        self.expected_outputs = []
        self.layer_inputs = []
        self.learning_rate = 0
        self.layer_error = 0
        for i in range(0, number_neurons):
            temp_neuron = Neuron.Neuron(number_connections)
            self.add_neuron(temp_neuron)
            self.add_actual_output()

    @classmethod
    def add_neuron(self, xneuron):
        """
        Function to add an input or output Neuron to this Layer
        :param xneuron:
        :return:
        """
        self.neurons.append(xneuron)

    @classmethod
    def get_neuron_count(self):
        """
        Function to get the number of neurons in this layer
        :return:
        """
        return len(self.neurons)

    @classmethod
    def add_actual_output(self):
        """
        Function to increment the size of the actualOUTPUTs array by one.
        :return:
        """
        self.actual_output.append(None)

    @classmethod
    def set_expected_outputs(self, temp_expected_outputs):
        """
        Function to set the ENTIRE expected OUTPUTs array in one go.
        :param temp_expected_outputs:
        :return:
        """
        self.expected_outputs = temp_expected_outputs

    @classmethod
    def clear_expected_output(self):
        """
        Function to clear ALL values from the expectedOUTPUTs array
        :return:
        """
        self.expected_outputs = []

    @classmethod
    def set_learing_rate(self, temp_learning_rate):
        """
        Function to set the learning rate of the layer
        :param temp_learning_rate:
        :return:
        """
        self.learning_rate = temp_learning_rate

    @classmethod
    def set_inputs(self, temp_inputs):
        """Function to set the inputs of this layer"""
        self.layer_inputs = temp_inputs

    @classmethod
    def process_inputs_to_outputs(self):
        """
        Function to convert ALL the Neuron input values into Neuron output values in this layer, through a special activation function.
        :return:
        """
        neuronCount = self.get_neuron_count()
        if neuronCount > 0:
            if len(self.layer_inputs) != self.neurons[0].get_connection_count():
                print "Error in Layer: processInputsToOutputs: The number of inputs do NOT match the number of Neuron connections in this layer"
                exit()
            else:
                for i in range(0, neuronCount):
                    self.actual_output[i] = self.neurons[i].get_neuron_output(self.layer_inputs)
        else:
            print "Error in Layer: processInputsToOutputs: There are no Neurons in this layer"
            exit()

    @classmethod
    def get_layer_error(self):
        """
        Function to get the error of this layer
        :return:
        """
        return self.layer_error

    @classmethod
    def set_layer_error(self, temp_layer_error):
        """
        Function to set the error of this layer
        :param temp_layer_error:
        :return:
        """
        self.layer_error = temp_layer_error

    @classmethod
    def increase_layer_error_by(self, temp_layer_error):
        """
        Function to increase the layerError by a certain amount
        :param temp_layer_error:
        :return:
        """
        self.layer_error += temp_layer_error

    @classmethod
    def set_delta_error(self, expected_output_data):
        """
        Function to calculate and set the deltaError of each neuron in the layer
        :param expected_output_data:
        :return:
        """
        self.set_expected_outputs(expected_output_data)
        neuron_count = self.get_neuron_count()
        self.set_layer_error(0)
        for i in range(0, neuron_count):
            self.neurons[i].delta_error = self.actual_output[i] * (1-self.actual_output[i]) * (self.expected_outputs[i] - self.actual_output[i])
            self.increase_layer_error_by(abs(self.expected_outputs[i] - self.actual_output[i]))

    @classmethod
    def train_layer(self, temp_learning_rate):
        """
        Function to train the layer : which uses a training set to adjust the connection weights and biases of the neurons in this layer
        :param temp_learning_rate:
        :return:
        """
        self.set_learing_rate(temp_learning_rate)
        neuron_count = self.get_neuron_count()
        for i in range(0, neuron_count):
            self.neurons[i].bias += (self.learning_rate * 1 * self.neurons[i].delta_error)
            for j in range(0, self.neurons[i].get_connection_count()):
                self.neurons[i].connections[j].weight += (self.learning_rate * self.neurons[i].connections[j].conn_entry * self.neurons[i].delta_error)



