import Layer
import random

class NeuralNetwork:

    def __init__(self):
        self.layers = []
        self.array_of_inputs = []
        self.array_of_outputs = []
        self.learning_rate = 0.1
        self.network_error = 0
        self.training_error = 0
        self.retrain_chances=0

    def add_layer(self, num_connections, num_neurons):
        self.layers.append(Layer(num_connections, num_neurons))

    def get_layer_count(self):
        return len(self.layers)

    def set_learning_rate(self, temp_learning_rate):
        self.learning_rate = temp_learning_rate

    def set_inputs(self, temp_inputs):
        self.array_of_inputs = temp_inputs

    def set_layer_inputs(self,temp_inputs, layer_index):
        if layer_index > self.get_layer_count() -1:
            print "NN Error: setLayerInputs: layerIndex=" + layer_index + " exceeded limits= " + str(self.get_layer_count() -1)
        else:
            self.layers[layer_index].set_inputs(temp_inputs)

    def set_outputs(self, temp_outputs):
        self.array_of_outputs = temp_outputs

    def get_outputs(self):
        return self.array_of_outputs

    def process_inputs_to_outputs(self, temp_inputs):
        self.set_inputs(temp_inputs)
        if self.get_layer_count > 0:
            if len(self.array_of_inputs) != self.layers[0].neurons[0].get_connected_count():
                print "NN Error: processInputsToOutputs: The number of inputs do NOT match the NN"
                exit()
            else:
                for i in range(0 , self.get_layer_count()):
                    if i ==0:
                        self.set_layer_inputs(self.array_of_inputs,i)
                    else:
                        self.set_layer_inputs(self.layers[i-1].actual_outputs, i)

                    self.layers[i].process_inputs_to_outputs()

                self.set_outputs(self.layers[self.get_layer_count()-1].actual_outputs)
        else:
            print "Error: There are no layers in this Neural Network"
            exit()

    def train_network(self, input_data, expected_output_data):
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

                    self.layers[i].neurons[j].delta_error = (self.layers[i].neuron_output_value * (1-self.layers[i].neurons[j].neuron_output_value))
                self.layers[i].train_layer(self.learning_rate)
                self.layers[i].clear_expected_output()

    def training_cycle(self, training_input_data, training_expected_data, train_randomly):
        dataindex = 0
        training_error = 0
        for i in range(0, len(training_input_data)):
            if train_randomly:
                dataindex = random(0, len(training_input_data))
            else:
                dataindex = i

            self.train_network((training_input_data[i], training_expected_data[i],))
            training_error += abs(self.network_error)

    def auto_train_network(self,training_input_data, training_expected_data, training_error_target, cycle_limit):
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

