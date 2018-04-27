import pickle

unpickled = pickle.load(open("files/banner.p", "rb"))
print(unpickled)
for i in unpickled:
    for j in i:
        print(j[1]*j[0],end="")
    print(" ")