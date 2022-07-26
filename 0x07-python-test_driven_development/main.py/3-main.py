say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("john", "string")
"""
>>> say_my_name("john", "string")
My name is john string
"""

say_my_name("John")
"""
>>> say_my_name("john")
My name is john
"""

say_my_name( ,"jog")
"""
>>> say_my_name(, "jog")
Traceback (most recent call)
SyntaxError: first_name must be a string
"""

try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
try:
    say_my_name( ,"john")
except Exception as ex:
    print(ex)
