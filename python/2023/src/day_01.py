from typing import List


def extract_two_digit_number(input: str) -> int:
    number: List[str] = []

    for c in input:
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number.append(c)

    if len(number) < 1:
        return 0

    return int("".join([number[0], number[len(number) - 1]]))


if __name__ == "__main__":
    total = 0

    with open("./python/2023/src/day_01_input.txt", "r") as f:
        for line in f:
            total += extract_two_digit_number(line)

    print(total)
