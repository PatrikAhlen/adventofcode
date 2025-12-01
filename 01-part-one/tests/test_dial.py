from dial import Dial
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestDial(unittest.TestCase):
    def test_input_file_format(self):
        import re
        with open(os.path.join(os.path.dirname(__file__), '../01-input.txt')) as f:
            for line in f:
                line = line.strip()
                self.assertRegex(
                    line, r'^[RL][0-9]+$', f"Invalid format: {line}")

    def test_process_commands(self):
        dial = Dial(start=0)
        commands = ["R10", "L5", "R95", "R5"]  # 0->10->5->0->5
        for cmd in commands:
            direction = cmd[0]
            steps = int(cmd[1:])
            dial.turn(direction, steps)
        self.assertEqual(dial.value, 5)
        self.assertEqual(dial.zero_counter, 1)  # Lands on 0 once

    def test_zero_counter_increments(self):
        dial = Dial(start=95)
        dial.turn('R', 5)  # Lands on 0
        self.assertEqual(dial.value, 0)
        self.assertEqual(dial.zero_counter, 1)

    def test_turn_left(self):
        dial = Dial(start=5)
        dial.turn('L', 10)  # Should wrap around: 5 - 10 = -5 -> 95
        self.assertEqual(dial.value, 95)

    def test_set_start_value(self):
        dial = Dial(start=42)
        self.assertEqual(dial.value, 42)

    def test_initial_zero_counter(self):
        dial = Dial(start=10)
        self.assertEqual(dial.zero_counter, 0)

    def test_turn_right(self):
        dial = Dial(start=90)
        dial.turn('R', 15)  # Should wrap around: 90 + 15 = 105 -> 5
        self.assertEqual(dial.value, 5)


if __name__ == "__main__":
    unittest.main()
