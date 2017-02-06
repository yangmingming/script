#True
print True and True

#False
print False and True

#False
print 1 == 1 and 2 == 1

#True
print "test" == "test"

#True
print 1 == 1 and 2 != 1

#True
print True and 1 == 1

#False
print False and 0 != 0

#True
print True or 1 == 1

#False
print "test" == "testing"

#False
print 1 != 0 and 2 == 1

#True [error]
print "test" != "testing"

""" True / False 是布尔变量，和字符串相比都是假 """
#False [error]
print "test" == 1

#True
print not (True and False)

print "--------"

print not (True and False)
#True

print not (1 == 1 and 0 != 1)
#False

print not (10 == 1 or 1000 == 1000)
#False

print not (1 != 10 or 3 == 4)
#False

print not ("testing" == "testing" and "Zed" == "Cool guy")
#True

#True [error]
print 1 == 1 and (not ("testing" == 1 or 1 == 0))

print "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
#False

print 3 == 3 and (not ("testing" == "testing" or "Python" == "fun"))
#False
