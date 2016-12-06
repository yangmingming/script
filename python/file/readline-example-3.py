from sys import argv

script, file = argv

fd = open(file)

while 1:
    lines = fd.readlines(100000)
    if not lines:
        break
    for line in lines:
        pass    #do something

fd.close()
