import string

def caesar(s, shift = 2):
    alphabet = [l for l in string.ascii_lowercase]
    translated = ""

    for letter in s:
        if letter in alphabet:
            translated += alphabet[(alphabet.index(letter)+shift)%len(alphabet)]
        else:
            translated += letter

    return translated

#s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
#    "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = "map.html"
print(caesar(s))