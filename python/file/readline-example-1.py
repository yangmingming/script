from sys import argv

script, file = argv

fd = open(file)

while 1:
    line = fd.readline()
    if not line:
        break
    pass    #do something

fd.close()
