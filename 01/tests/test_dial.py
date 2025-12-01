from dial import Dial
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestDial(unittest.TestCase):
    def test_zero_counter_lands_on_zero(self):
        # Should increment zero_counter when landing exactly on 0
        dial = Dial(start=10)
        dial.turn('L', 10)  # 10 -> 0, lands on 0
        self.assertEqual(dial.value, 0)
        self.assertEqual(dial.zero_counter, 1)

        dial = Dial(start=90)
        dial.turn('R', 10)  # 90 -> 0, lands on 0
        self.assertEqual(dial.value, 0)
        self.assertEqual(dial.zero_counter, 1)

    def test_zero_counter_lands_and_passes_zero(self):
        # Should only increment once if both passing and landing on 0 in one move
        dial = Dial(start=95)
        dial.turn('R', 105)  # 95 -> 0, passes and lands on 0
        self.assertEqual(dial.value, 0)
        self.assertEqual(dial.zero_counter, 2)

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
        # 0->10 (no pass), 10->5 (no pass), 5->0 (passes 0 once), 0->5 (no pass)
        self.assertEqual(dial.zero_counter, 1)

    def test_process_commands_facit(self):
        dial = Dial(start=50)
        # 50->82->52->0->95->55->0->99->0->14->32
        commands = ["L68", "L30", "R48", "L5",
                    "R60", "L55", "L1", "L99", "R14", "L82"]
        for cmd in commands:
            direction = cmd[0]
            steps = int(cmd[1:])
            dial.turn(direction, steps)
        self.assertEqual(dial.value, 32)
        # 0->10 (no pass), 10->5 (no pass), 5->0 (passes 0 once), 0->5 (no pass)
        self.assertEqual(dial.zero_counter, 6)

    def test_zero_counter_increments(self):
        dial = Dial(start=95)
        dial.turn('R', 10)  # 95->5, passes 0 once
        self.assertEqual(dial.value, 5)
        self.assertEqual(dial.zero_counter, 1)

        dial = Dial(start=50)
        dial.turn('L', 55)  # 50->95, passes 0 once
        self.assertEqual(dial.value, 95)
        self.assertEqual(dial.zero_counter, 1)

        # 95->5, passes 0 twice (95->99, 0, 1->99, 0, 1->5)
        dial.turn('R', 110)
        self.assertEqual(dial.value, 5)
        self.assertEqual(dial.zero_counter, 3)

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

    def test_turn_passing_zero_multiple_times(self):
        dial = Dial(start=0)
        dial.turn('R', 250)  # 0 -> 50, passes 0 two times
        self.assertEqual(dial.value, 50)
        self.assertEqual(dial.zero_counter, 2)

        dial.turn('L', 50)  # 50 -> 0, lands on 0
        self.assertEqual(dial.value, 0)
        self.assertEqual(dial.zero_counter, 3)

        dial.turn('R', 150)  # 0 -> 50, passes 0 one time
        self.assertEqual(dial.value, 50)
        self.assertEqual(dial.zero_counter, 4)


if __name__ == "__main__":
    unittest.main()
