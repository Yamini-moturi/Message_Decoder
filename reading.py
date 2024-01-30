def print_pyramid(rows):
    count=1
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print numbers in increasing order
        for j in range(1, i + 1):
            print(count, end=" ")
            count+=1

        # Move to the next line for the next row
        print()

# Example usage:
pyramid_rows = 3  # Replace with the desired number of rows
print_pyramid(pyramid_rows)
