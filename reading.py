
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
