def caesarCipher(s, k):
    output = []
    for letter in s:
        num = ord(letter)
        if num in range(97, 123):
            output.append(chr(((num-97+k)%26)+97))
        elif num in range(65, 91):
            output.append(chr(((num-65+k)%26)+65))
        else:
            output.append(letter)
    return "".join(output)
