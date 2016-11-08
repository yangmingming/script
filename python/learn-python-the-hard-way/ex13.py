from sys import argv

file, a1, a2, a3 = argv

print "This file %s's param is %s %s %s" %(file, a1, a2, a3)

"""
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    file, a1, a2, a3 = argv
ValueError: need more than 1 value to unpack
"""
