from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We will use script %s copy %s to %s" %(script, from_file, to_file)
print "Are you sure ?"
print "You can press CTRL+C to exit"
raw_input()

print "%s is exists ? %r" %(to_file, exists(to_file))

fd = open(from_file)
str = fd.read()
fd.close()
length = len(str)
print "%s has %s chars" %(from_file, length)

fd_out = open(to_file, "w");
fd_out.write(str)
fd_out.close()        
print "Copy success!!!"
