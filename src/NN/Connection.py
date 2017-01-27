import random

class Connection:

    def __init__(self, temp_weight = None):
        self.conn_entry = 0
        self.weight = 0
        self.connExit = 0
        self.randomise_weight()
        if temp_weight is not None:
            self.set_weight(temp_weight)


    def set_weight(self, temp_weight):
        self.weight = temp_weight

    def randomise_weight(self):
        self.set_weight(random.uniform(0, 1))

    def calc_conn_exit(self, temp_input):
        self.conn_entry = temp_input
        self.connExit = self.conn_entry * self.weight
        return self.conn_entry
