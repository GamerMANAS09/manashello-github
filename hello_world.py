message = "helloworld"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# First part: constructing the string from the alphabet without delay
for i in range(len(message)):
    for j in range(len(alphabet)):
        if i == 0:  # Only print the first character of the message at position 0
            current_str = message[:i+1]
        else:
            prefix = alphabet[j]
            current_str = prefix + message[:i+1]
        print(current_str)
        if current_str == message[:i+1]:
            break

# Second part: constructing the string from the alphabet with prefix and suffix without delay
for k in range(len(alphabet)):
    prefix = alphabet[k]
    current_str = prefix + message + prefix
    print(current_str)
    if current_str == prefix + message + prefix:
        break
