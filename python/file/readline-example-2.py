from sys import argv
import fileinput

script, file = argv

for line in fileinput.input(file):
    pass    #do something
