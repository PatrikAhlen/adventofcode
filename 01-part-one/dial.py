class Dial:
    def __init__(self, start=0):
        self.value = start
        self.zero_counter = 0

    def turn(self, direction, steps):
        if direction == 'R':
            self.value = (self.value + steps) % 100
        elif direction == 'L':
            self.value = (self.value - steps) % 100
        if self.value == 0:
            self.zero_counter += 1
