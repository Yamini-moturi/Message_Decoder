import math
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
    file_path = "smallinputs.txt"  # Replace with the actual file path
    key_value_pairs = readfile_createdict(file_path)
    linecount=len(key_value_pairs) #calculating the line count of files
    rows=calculate_rows(linecount)
    count=1
    last_numbers=[] #storing the last numbers of each pyramid.
    for i in range(1,rows+1):
        for j in range(1, i + 1):
            #print(count, end=" ") testing
            last_num=count
            count += 1
        last_numbers.append(last_num)
    #end of gathers the last numbers from pyramids
    for key in last_numbers:
        if key in key_value_pairs:
            print(f"{key_value_pairs[key]}", end=" ") #prints the decoded message.
    