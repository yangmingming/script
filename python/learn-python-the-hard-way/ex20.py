from sys import argv

script, file = argv

def print_all(fd):
    print fd.read()

def file_seek(fd):
    fd.seek(0)

def print_line(line, fd):
    print "line %d: %s" %(line, fd.readline())
def print_line2(line, fd):
    print "line %d: %s" %(line, fd.readline()),

fd = open(file)
print "show all comment:"
print_all(fd)

print "seek 0"
file_seek(fd)

print "print three lines first:"
line = 1
print_line(1, fd)

line += 1
print_line(1, fd)

line += 1
print_line(1, fd)

print "seek 0"
file_seek(fd)

print "print three lines second:"
line = 1
print_line2(1, fd)

line += 1
print_line2(1, fd)

line += 1
print_line2(1, fd)
