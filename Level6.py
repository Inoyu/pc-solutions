import zipfile

zf = zipfile.ZipFile("files/channel.zip", "r")

def decodeZip(zipFile, startNum, files = []):
    direction = "files/channel/" + str(startNum) + ".txt"
    try:
        with open(direction, "r") as file:
            files.append(str(startNum) + ".txt")
            line = file.read()
        decodeZip(zipFile, [int(i) for i in line.split() if i.isdigit()][0], files)
    except:
        print("Decoded all files")

    return [zf.getinfo(f).comment.decode("utf-8") for f in files]

for char in decodeZip(zf, 90052):
    print(char, end="")
zf.close()


