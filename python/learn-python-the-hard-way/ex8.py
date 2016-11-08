# -*- encoding: utf-8 -*-
format = "%r, %r, %r, %r"

#number
print format %(1, 2, 3, 4)

#char
print format %('y', 'm', 'm', 'm')

#string
print format %("ymm", "how", "are", "you")
print format %("中国", "how", "are", "you")
print "%s, %r, %r, %r" %("中国", "how", "are", "you")

#bool
print format %(True, False, False, True)

print format %(format, format, format, format)

#coment
print format %(
            "first comment",
            "second comment",
            "third comment",
            "ymm's comment"
            )
