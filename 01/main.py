import sys
from dial import Dial


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_file> [start_value]")
        sys.exit(1)
    input_file = sys.argv[1]
    start_value = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    dial = Dial(start=start_value)
    with open(input_file) as f:
        for line in f:
            cmd = line.strip()
            if not cmd:
                continue
            direction = cmd[0]
            steps = int(cmd[1:])
            prev_value = dial.value
            dial.turn(direction, steps)
            hit_zero = dial.value == 0 and prev_value != 0
            print(f"Turn: {cmd:6} | Dial: {prev_value:2} -> {dial.value:2}" +
                  ("  <== HIT 0!" if hit_zero else ""))
    print(f"Final dial value: {dial.value}")
    print(f"Zero-counter: {dial.zero_counter}")


if __name__ == "__main__":
    main()
