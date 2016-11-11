from sys import argv

script, file = argv 
print "Are you sure clear the file %s" %file
print "If you don't want, you can press Ctrl + C "

raw_input("?")

"""
Modes   Description
r   Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
r+  Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
w   Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+  Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a   Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+  Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

rb  Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
rb+ Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
wb  Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
ab  Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

https://www.tutorialspoint.com/python/python_files_io.htm
"""
fd = open(file, "w")
#fd = open(file, "r")
#fd.truncate()
print "truncate success"

print "input three lines"
line1 = raw_input("line 1 > ")
line2 = raw_input("line 2 > ")
line3 = raw_input("line 3 > ")

fd.write(line1)
fd.write("\n")
fd.write(line2)
fd.write("\n")
fd.write(line3)
fd.write("\n")

fd.close()
