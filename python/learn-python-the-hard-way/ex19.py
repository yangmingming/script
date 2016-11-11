def print_fruit(apple, orange):
    print "apple: %s" %apple
    print "orange: %s" %orange
    print "\n"

print "use num directly"
print_fruit(10, 20)

print "use variable"
a = 30
b = 40
print_fruit(a, b)

print "use math operator"
print_fruit(10 + 2, 10 + 4)

print "use variable and math operator"
print_fruit(a + 10, b + 3)
