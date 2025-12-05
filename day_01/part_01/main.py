dial = 50
num_of_zeros_reached = 0

def dialCalc(incoming_dial):
    if incoming_dial < 0:
        return 100 - abs(incoming_dial)

    elif incoming_dial == 100:
        return 0

    elif incoming_dial > 100:
        return incoming_dial - 100

    else:
        return incoming_dial

try:
    with open("./input.txt", "r") as file:
        for line in file:
            direction = line[0]
            amount = int(line[1:len(line)])

            if direction == "L":
                dial -= amount
            else:
                dial += amount

            while dial > 99 or dial < 0:
                dial = dialCalc(dial)

            if dial == 0:
                num_of_zeros_reached += 1

except FileNotFoundError:
    print("Error: The file for input.txt was not found")
except Exception as e:
    print(f"Error:  An unexpected error: {e}")

print(f"Num of zeros reached: {num_of_zeros_reached}")


