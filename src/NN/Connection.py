import random

class Connection:

    def __init__(self, temp_weight = None):
        """
        This is the defaukt constructor for a Connection
        :param temp_weight:
        """
        self.conn_entry = 0
        self.weight = 0
        self.connExit = 0
        self.randomise_weight()
        if temp_weight is not None:
            self.set_weight(temp_weight)

    @classmethod
    def set_weight(self, temp_weight):
        """
        A custon weight for this Connection constructor
        :param temp_weight:
        :return:
        """
        self.weight = temp_weight

    @classmethod
    def randomise_weight(self):
        """
        Function to set the weight of this connection
        :return:
        """
        self.set_weight(random.uniform(0, 1))

    @classmethod
    def calc_conn_exit(self, temp_input):
        """
        Function to calculate and store the output of this Connection
        :param temp_input:
        :return:
        """
        self.conn_entry = temp_input
        self.connExit = self.conn_entry * self.weight
        return self.conn_entry
