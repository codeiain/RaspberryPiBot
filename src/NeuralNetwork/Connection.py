import random

class Connection:

    def __init__(self):
        self.connEntry = 0
        self.weight = 0
        self.connExit = 0
        self.randomise_weight()

    def __init__(self, temp_weight):
        self.connEntry = 0
        self.weight = 0
        self.connExit = 0
        self.randomise_weight()
        self.set_weight(temp_weight)

    def set_weight(self, temp_weight):
        self.weight = temp_weight

    def randomise_weight(self):
        self.set_weight(random.uniform(0, 1))

    def calc_conn_exit(self, temp_input):
        self.connEntry = temp_input
        self.connExit = self.connEntry * self.weight
        return self.connExit
