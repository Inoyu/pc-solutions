def rarity(filename):
    with open(filename, "r") as file:
        s = file.read().replace("\n", "")

    rarity = {}
    rareString = ""

    for char in s:
        if char not in rarity:
            rarity[char] = 1
        else:
            rarity[char] += 1

    for keys in rarity:
        if rarity[keys] == 1:
            rareString += keys

    file.close()
    return rareString

print(rarity("files/RareCharData.txt"))
