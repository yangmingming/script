def print_two(*args):
    v1, v2 = args
    print "first param: %s, secode param %s" %(v1, v2)

def print_two_again(v1, v2):
    print "first param: %s, secode param %s" %(v1, v2)

def print_one(v1):
    print "first param: %s" %v1
"""
  File "ex18.py", line 8
        def print_one(v1)
                        ^
    SyntaxError: invalid syntax
"""

def print_none():
    print "no prame"

print_two("yang", "ming")
print_two_again("yang", "ming")
print_one("yang")
print_none()
