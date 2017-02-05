print "Let's exercise something"

print 'This is one first line.\nThe next line and \tone tabs.\nThen output \\ and one \' and one "'

poem = """
Today is a wonderful day.\nand
Tomorrow is also one good day.\nIf you believe,
everyday is a good day.
"""

print "===================="
print poem
print "===================="

def fun(num):
    add = num + 10
    sub = add - 3
    mul = sub * 20
    div = mul / 5
    return add, sub, mul, div

first = 20
one, two, three, four = fun(first)
print "fist %d" %first
print "%d %d %d %d" %(one, two, three, four)

second = first / 5
print "second %d" %second
print "%d %d %d %d" % fun(second)
print fun(second)
        
"""
Traceback (most recent call last):
  File "ex23.py", line 12, in <module>
    print peom
NameError: name 'peom' is not defined

  File "ex23.py", line 30
    print "%d %d %d %d" fun(second)
                          ^
SyntaxError: invalid syntax
"""
