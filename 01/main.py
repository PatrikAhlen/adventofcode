import sys
from dial import Dial


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python3 main.py <input_file> [start_value] [output_file]")
        sys.exit(1)
    input_file = sys.argv[1]
    start_value = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    output_file = sys.argv[3] if len(sys.argv) > 3 else "result.txt"
    dial = Dial(start=start_value)
    output_lines = []
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
            out_line = f"Turn: {cmd:6} | Dial: {prev_value:2} -> {dial.value:2} | Zero passes: {dial.zero_counter}" + (
                "  <== HIT 0!" if hit_zero else "")
            print(out_line)
            output_lines.append(out_line)
    final1 = f"Final dial value: {dial.value}"
    final2 = f"Zero-counter: {dial.zero_counter}"
    print(final1)
    print(final2)
    output_lines.append(final1)
    output_lines.append(final2)
    with open(output_file, 'w') as outf:
        for line in output_lines:
            outf.write(line + '\n')


if __name__ == "__main__":
    main()
