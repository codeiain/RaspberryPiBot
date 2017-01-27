import Neuron


class Layer:

    def __init__(self, number_connections, number_neurons):
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

    def add_neuron(self, xneuron):
        self.neurons.append(xneuron)

    def get_neuron_count(self):
        return len(self.neurons)

    def add_actual_output(self):
        self.actual_output.append(None)

    def set_expected_outputs(self, temp_expected_outputs):
        self.expected_outputs = temp_expected_outputs

    def clear_expected_output(self):
        self.expected_outputs = []

    def set_learing_rate(self, temp_learning_rate):
        self.learning_rate = temp_learning_rate

    def set_inputs(self, temp_inputs):
        self.layer_inputs = temp_inputs

    def process_inputs_to_outputs(self):
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
            exit();

    def get_layer_error(self):
        return self.layer_error

    def set_layer_error(self, temp_layer_error):
        self.layer_error = temp_layer_error

    def increase_layer_error_by(self, temp_layer_error):
        self.layer_error += temp_layer_error

    def set_delta_error(self, expected_output_data):
        self.set_expected_outputs(expected_output_data)
        neuron_count = self.get_neuron_count()
        self.set_layer_error(0)
        for i in range(0, neuron_count):
            self.neurons[i].delta_error = self.actual_output[i] * (1-self.actual_output[i]) * (self.expected_outputs[i] - self.actual_output[i])
            self.increase_layer_error_by(abs(self.expected_outputs[i] - self.actual_output[i]))

    def train_layer(self, temp_learning_rate):
        self.set_learing_rate(temp_learning_rate)
        neuron_count = self.get_neuron_count()
        for i in range(0, neuron_count):
            self.neurons[i].bias += (self.learning_rate * 1 * self.neurons[i].delta_error)
            for j in range(0, self.neurons[i].get_connection_count()):
                self.neurons[i].connections[j].weight += (self.learning_rate * self.neurons[i].connections[j].conn_entry * self.neurons[i].delta_error)



