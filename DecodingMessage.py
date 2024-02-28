def decode(message_file):
    pyramid_lines = []

    # Read the file and store each line as a tuple (number, word)
    with open(message_file, 'r') as file:
        pyramid_lines = [line.strip().split(' ', 1) for line in file]

    decoded_message = []

    # Iterate through the pyramid lines to extract the words at the specified numbers
    for i, line in enumerate(pyramid_lines):
        num = int(line[0])
        word = line[1]

        # Check if the number is at the end of the current line or in the middle
        if i == 0 or i == len(pyramid_lines) - 1:
            decoded_message.append(word)
        else:
            decoded_message.append(word if num % 2 != 0 else '')

    # Return the decoded message as a string, removing any empty strings
    return ' '.join(filter(None, decoded_message))

# Example usage:
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)