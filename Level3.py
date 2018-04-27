import string
def bodyguard(textfile):
    with open(textfile, "r") as file:
        s = file.read().replace("\n", "")
    solution = ""
    counter = 0


    for i in range(3, len(s)-3):
        if s[i] in string.ascii_lowercase:
            for j in range(1, 5):
                if j == 4:
                    if s[i-j] in string.ascii_lowercase and s[i+j] in string.ascii_lowercase:
                        counter += 1
                elif s[i-j] in string.ascii_uppercase and s[i+j] in string.ascii_uppercase:
                    counter += 1
                else:
                    break
            if counter == 4:
                solution += s[i]
            counter = 0

    file.close()
    return solution

print(bodyguard("files/bodyguard.txt"))
