f = open("test.txt","r")

c = f.read()
if ("twinkal" in c):
    print(True)
f.close()