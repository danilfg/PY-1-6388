# int, float, hex, ord, bin
# type() function
# import math

# >>> number = 10
# >>> int(number)
# 10
# >>> float(number)
# 10.0
# >>> type(number)
# <class 'int'>
# >>> type(float(number))
# <class 'float'>
# >>> 'a' < 'A'
# False
# >>> type('a')
# <class 'str'>
# >>> 'A' < 'a'
# True
# >>> ord('A')
# 65
# >>> ord('a')
# 97
# >>> max(540)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> max(['5','4','0'])
# '5'
# >>> max(['5','4','0',' ','.'])
# '5'
# >>> min(['5','4','0',' ','.'])
# ' '
# >>> bin(10)
# '0b1010'
# >>> type(bin(10))
# <class 'str'>
# >>> int('0b1010')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '0b1010'
# >>> int('0b1010', 2)
# 10
# >>> hex(16)
# '0x10'
# >>> hex(17)
# '0x11'
# >>> hex(400)
# '0x190'
# >>> int(hex(400), 16)
# 400
