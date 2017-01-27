import Connection
from math import exp
import random


class Neuron:
    @classmethod
    def __init__(self, num_of_connections=None):
        """
        The typical constructor of a Neuron - with random Bias and Connection weights
        :param num_of_connections:
        """
        self.connections = []
        self.bias = 0
        self.neuron_input_value = 0
        self.neuron_output_value = 0
        self.detla_error = 0
        if num_of_connections is not None:
            self.random_bias()
            for i in range(0, num_of_connections):
                conn = Connection.Connection()
                self.add_connection(conn)

    @classmethod
    def random_bias(self):
        """
        Function to add a Connection to this neuron
        """
        self.set_bias(random.uniform(0, 1))

    @classmethod
    def add_connection(self, conn):
        """
        Function to return the number of connections associated with this neuron.
        :param conn:
        """
        self.connections.append(conn)

    @classmethod
    def get_connection_count(self):
        """
        Function to set the bias of this Neuron
        """
        return len(self.connections)

    @classmethod
    def set_bias(self, temp_bias):
        """
        Function to randomise the bias of this Neuron
        :param temp_bias:
        """
        self.bias = temp_bias

    @classmethod
    def get_neuron_output(self, conn_entry_values):
        """
        Function to convert the neuronInputValue to an neuronOutputValue\n
        Make sure that the number of connEntryValues matches the number of connections
        :param conn_entry_values:
        :return:
        """
        if len(conn_entry_values) != self.get_connection_count():
            print "Neuron Error: getNeuronOutput() : Wrong number of connEntryValues"
            exit()
        neuron_input_value = 0

        for i in range(0, self.get_connection_count()):
            neuron_input_value += self.connections[i].calc_conn_exit(conn_entry_values[i])

        neuron_input_value += self.bias

        neuron_input_value = self.activation(neuron_input_value)

        return neuron_input_value

    @staticmethod
    def activation(x):
        """
        Sigmoid Activation function
        :param x:
        :return:
        """
        activation_value = 1 / (1 + exp(-1 * x))
        return activation_value

