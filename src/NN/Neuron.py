import Connection
from math import exp
import random


class Neuron:

    def __init__(self):
        self.connections = []
        self.bias = 0
        self.neuron_input_value = 0
        self.neuron_output_value = 0
        self.deltaError = 0

    def __init__(self, num_of_connections):
        self.connections = []
        self.bias = 0
        self.neuron_input_value = 0
        self.neuron_output_value = 0
        self.deltaError = 0
        self.random_bias()
        for i in range(0, num_of_connections):
            conn = Connection()
            self.add_connection(conn)

    def random_bias(self):
        self.set_bias(random(0, 1))

    def add_connection(self, conn):
        self.connections.append(conn)

    def get_connection_count(self):
        return list.count(self.connections)

    def set_bias(self, temp_bias):
        self.bias = temp_bias

    def get_neuron_output(self, conn_entry_values):
        if list.count(conn_entry_values) != self.get_connection_count():
            print "Neuron Error: getNeuronOutput() : Wrong number of connEntryValues"
            exit()
        neuron_input_value = 0

        for i in range(0, self.get_connection_count()):
            neuron_input_value += self.connections[i].calc_conn_exit(conn_entry_values[i])

        neuron_input_value += self.bias

        neuron_input_value = self.activation(neuron_input_value)

        return neuron_input_value

    @staticmethod
    def activation(self, x):
        activation_value = 1 / (1 + exp(-1 * x))
        return activation_value

