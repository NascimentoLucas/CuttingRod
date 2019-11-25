class Data:
    def __init__(self):
        self.debug = False
        self.size = 0
        self.time_top_down = 0
        self.time_bottom_up = 0

    def data_print(self):
        s = str(self.size)
        s += ';' + str(self.time_top_down)
        s += ';' + str(self.time_bottom_up)
        print(s)

    @staticmethod
    def data_print_model():
        s = 'size'
        s += ';time_top_down'
        s += ';time_bottom_up'
        print(s)
