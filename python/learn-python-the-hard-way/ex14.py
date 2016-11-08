from sys import argv

script, name = argv

prompt = "> "

print "My name is %s, and I run the script %s" %(name, script)

print "What's your name ?"
my_name = raw_input(prompt)

print "What's your age ?"
my_age= int(raw_input(prompt))

print "Where are you from ?"
my_addr= raw_input(prompt)

print """
name: %s
age:  %d
addr: %s
""" %(my_name, my_age, my_addr)
