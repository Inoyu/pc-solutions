from PIL import Image
try:
    img = Image.open("files/oxygen.png")
    px = img.load()
    width = img.width
    height = img.height/2 #grey bar
    greyPixels = [px[x, height] for x in range(0, width, 7)]
    answer = "".join([chr(i[0]) for i in greyPixels if i[0] == i[1] == i[2]])
    print(answer)
    print("".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))) #list is found within the answer string

except:
    print("Unable to load image")

