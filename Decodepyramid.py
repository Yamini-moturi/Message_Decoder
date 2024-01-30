import math

def read_file_and_create_dict(message_file):
    input_pairs = {}  # Initialize a dictionary to store key-value pairs from the input file

    # Read the input text file lines
    with open(message_file, 'r') as file:
        for line in file:
            # Split each line into a list [number, word]
            line_parts = line.strip().split()

            # Ensure the line is in the correct format (number followed by a word)
            if len(line_parts) == 2:
                number, word = line_parts
                input_pairs[int(number)] = word

    return input_pairs

def calculate_rows(total_values):
    # Using the quadratic formula to calculate the number of rows needed for given numbers.
    rows = (-1 + math.sqrt(1 + 8 * total_values)) / 2
    return int(rows)

if __name__ == "__main__":
    file_path = "coding_qual_input.txt"  # give the inputs file path or file name.
    key_value_pairs = read_file_and_create_dict(file_path)
    
    line_count = len(key_value_pairs)  # Calculating the line count of files
    rows = calculate_rows(line_count) #calculating the rows needed for the pyramid for the input file length

    last_numbers = []  # Storing the last numbers of each pyramid.
    count = 1

    for i in range(1,rows+1):
        for j in range(1, i + 1):
            #print(count, end=" ") #testing
            last_num=count
            count += 1
        last_numbers.append(last_num)
    # End of gathering the last numbers from pyramids

    decoded_message = ' '.join(key_value_pairs.get(key, '') for key in last_numbers)
    print(decoded_message)
