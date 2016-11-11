from sys import argv

script, file = argv

print "Your file name is %r" % file

txt = open(file)
content = txt.read()
print content
txt.close()

file2 = raw_input("> ")
txt2 = open(file2)
print txt2.read()
txt2.close()
