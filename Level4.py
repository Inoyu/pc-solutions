import urllib.request

def followTheChain(nothing):
    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    try:
        req = urllib.request.Request(link + str(nothing))
        with urllib.request.urlopen(req) as response:
            newNothing = response.read().decode("utf-8")

        print(newNothing)
        followTheChain(str([int(s) for s in newNothing.split() if s.isdigit()][0]))
    except:
        print("Reached the end")

x1 = 12345
x2 = 8022
followTheChain(x2)