def add(argv1, argv2):
    print "ADD (%d + %d)" %(argv1, argv2)
    return argv1 + argv2

def sub(argv1, argv2):
    print "SUB (%d - %d)" %(argv1, argv2)
    return argv1 - argv2

def mul(argv1, argv2):
    print "MUL (%d * %d)" %(argv1, argv2)
    return argv1 * argv2

def div(argv1, argv2):
    print "DIV (%d / %d)" %(argv1, argv2)
    return argv1 / argv2

a = add(1, 2)
b = sub(10, 7)
c = mul(2, 3)
d = div(10, 5)

print "add:%d, sub:%d, mul:%d, div:%d " %(a, b, c, d)

print add(1, sub(10, mul(2, div(32, 8))))

# 2 + 3 * 5 - 18 / 2
print add(2, sub(mul(3, 5), div(18, 2)))

num = float(raw_input("input one float num :"))
print "float num %f" %num
