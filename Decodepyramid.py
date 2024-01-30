def readfile_createdict(message_file):
    inputpairs={} # initialized a dictionary- to store the key value pairs of input file 
    # Read the input text file lines from the file
    with open(message_file, 'r') as file:
        for line in file:
            
            # Split each line into a list [number, word]
            line_parts = line.strip().split()

            # Ensure the line is in the correct format (number followed by a word)
            if len(line_parts) == 2:
                number, word = line_parts
                inputpairs[int(number)] = word

    return inputpairs

def calculate_rows(total_values):
    # Using the quadratic formula to calculate the number of rows
    rows = (-1 + math.sqrt(1 + 8 * total_values)) / 2
    return int(rows)


if __name__ == "__main__":
    file_path = "coding_qual_input.txt"  # Replace with the actual file path
    key_value_pairs = readfile_createdict(file_path)
    linecount=len(key_value_pairs) #calculating the line count of files
    rows=calculate_rows(linecount)
    print(linecount) 
   
  