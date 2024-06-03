message = "helloworld"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(message)):
    for j in range(len(alphabet)):
        prefix = alphabet[j]
        current_str = prefix + message[:i+1]
        if current_str == message:
            break
        print(current_str)
for k in range(len(alphabet)):
    prefix = alphabet[k]
    current_str = prefix + message[:i+1] + prefix
    if current_str == message:
        break
    print(current_str)