def decode(message_file):
    pyramid = []
    with open(message_file, 'r') as file:
        for line in file:
            line = line.strip().split()
            pyramid.append(line[1])

    decoded_message = ' '.join(pyramid)
    return decoded_message.lower()

decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
