import math

dial = 50
num_of_zeros_reached = 0
num_of_zero_clicks = 0
max_dial = 100
input_file_loc = "./input.txt"


def calculateDialMovement(amount):
    if amount >= max_dial:
        dial_movement = amount % max_dial
    else:
        dial_movement = amount

    return dial_movement


def dialCalculate(start_dial, direction, amount, num_of_zeroes_passed):
    dial_pos = start_dial
    rotations = 0
    dial_movement = 0

    if amount == 0:
        return [start_dial, num_of_zeroes_passed]

    if direction == "L":
        dial_movement = calculateDialMovement(amount)

        rotations = math.floor(amount / max_dial)

        if rotations >= 1:
            num_of_zeroes_passed += rotations

        dial_pos = dial_pos - dial_movement

        if dial_pos < 0:
            dial_pos = dial_pos + max_dial
            if start_dial != 0 and dial_pos != 0:
                num_of_zeroes_passed += 1

        return [dial_pos, num_of_zeroes_passed]

    if direction == "R":
        dial_movement = calculateDialMovement(amount)

        rotations = math.floor(amount / max_dial)

        if rotations >= 1:
            num_of_zeroes_passed += rotations

        dial_pos = dial_pos + dial_movement

        if dial_pos >= max_dial:
            dial_pos = dial_pos - max_dial
            if start_dial != 0 and dial_pos != 0:
                num_of_zeroes_passed += 1

        return [dial_pos, num_of_zeroes_passed]


try:
    with open(input_file_loc, "r") as file:
        for line in file:
            direction = line[0]
            amount = int(line[1 : len(line)])

            [dial, num_of_zero_clicks] = dialCalculate(
                dial, direction, amount, num_of_zero_clicks
            )

            if dial == 0:
                num_of_zeros_reached += 1
except FileNotFoundError:
    print("Error: The file for input.txt was not found")
except Exception as e:
    print(f"Error:  An unexpected error: {e}")

print(
    f"Num of zeros reached: {num_of_zeros_reached} + Num of zero clicks: {num_of_zero_clicks} = {num_of_zeros_reached + num_of_zero_clicks}"
)
