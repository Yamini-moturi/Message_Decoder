import math

def calculate_rows(total_values):
    # Using the quadratic formula to calculate the number of rows
    rows = (-1 + math.sqrt(1 + 8 * total_values)) / 2
    return int(rows)

def generate_pyramid(total_values):
    rows = calculate_rows(total_values)
    
    # Generate the pyramid
    count = 1
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print numbers in increasing order
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1

        # Move to the next line for the next row
        print()

# Example usage:
total_values = 300
generate_pyramid(total_values)
