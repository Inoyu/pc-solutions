def rarity(filename):
    with open(filename, "r") as file:
        s = file.read().replace("\n", "")

    rarity = {}
    final = ""

    for c in s:
        if c not in rarity:
            rarity[c] = 1
        else:
            rarity[c] += 1

    for keys in rarity:
        if rarity[keys] == 1:
            final += keys

    file.close()
    return final

print(rarity("files/RareCharData.txt"))
