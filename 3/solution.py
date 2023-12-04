# Need to practice mutlidimensional arrays problems first
def sumOfSchematicParts():
    result = 0
    with open("3/input.txt") as file:
        for line in file:
            print(len(line)) # All are 141 characters
            # Need to convert this to a NxN matrix so its easier to traverse probably
            # Then I need to check the 8 directions (if possible, need to take care of the edges)
            # If the value of any edge is not a point, then the value is valid
            # And I need to make sure to concatenate any continous digits until a different character is found horizontally
    return result

sumOfSchematicParts()