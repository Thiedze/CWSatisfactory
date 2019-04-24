
class Building():

    def __init__(self, id, name, input, output, time, power, input_amount, output_amount):
        self.id = id
        self.name = name
        self.input = input
        self.output = output
        # time in seconds
        self.time = time
        # power in MW
        self.power = power
        self.input_amount = input_amount
        self.output_amount = output_amount
        self.overclocks = 0
        self.count = 1

    def items_per_minute_input(self):
        return 60 / self.time * self.input_amount * self.count

    def items_per_minute_output(self):
        return 60 / self.time * self.output_amount * self.count