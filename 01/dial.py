class Dial:
    def __init__(self, start=0):
        self.value = start
        self.zero_counter = 0

    def turn(self, direction, steps):
        prev_value = self.value
        if direction == 'R':
            new_value = (self.value + steps) % 100
            # Only count passes after the first click, unless starting value is not 0
            passes = 0
            for i in range(1, steps + 1):
                pos = (prev_value + i) % 100
                if pos == 0:
                    passes += 1
        elif direction == 'L':
            new_value = (self.value - steps) % 100
            passes = 0
            for i in range(1, steps + 1):
                pos = (prev_value - i) % 100
                if pos == 0:
                    passes += 1
        else:
            new_value = self.value
            passes = 0
        self.zero_counter += passes
        self.value = new_value
