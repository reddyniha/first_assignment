# 1.Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
#
# first_two('Hello') ? 'He'
# first_two('abcdefg') ? 'ab'
# first_two('ab') ? 'ab'

# Answer

# a = input("Enter a string: ")
# if a.__len__() > 2:
#     print(a[0:2])
# if a.__len__() < 2:
#     print(a)


# 2.Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
#
# extra_end('Hello') ? 'lololo'
# extra_end('ab') ? 'ababab'
# extra_end('Hi') ? 'HiHiHi'

# Answer
# a = input("Enter a string: ")
# if a.__len__() >= 2:
#     print(3*a[-2:])
# else:
#     print("Given string is less than 2 chars")


# 3)Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
# first_half('WooHoo') ? 'Woo'
# first_half('HelloThere') ? 'Hello'
# first_half('abcdef') ? 'abc'
# # Answer
# a = input("Enter a string: ")
# print(a[0:round(len(a)/2)])

#4) Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
#
# without_end('Hello') ? 'ell'
# without_end('java') ? 'av'
# without_end('coding') ? 'odin'


# Answer

# a = input("Enter a string: ")
# print(a[1:-1])


# 5)Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# make_abba('Hi', 'Bye') ? 'HiByeByeHi'
# make_abba('Yo', 'Alice') ? 'YoAliceAliceYo'
# make_abba('What', 'Up') ? 'WhatUpUpWhat'

# Answer
# print("{0}{1}{1}{0}".format("hi","bye"))


# 6)Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
#
# combo_string('Hello', 'hi') ? 'hiHellohi'
# combo_string('hi', 'Hello') ? 'hiHellohi'
# combo_string('aaa', 'b') ? 'baaab
#
#
# # Answer
# a,b = ('aaa', 'b')
# if len(a)<len(b):
#     print("{0}{1}{0}".format(a,b))
# if len(a) > len(b):
#         print("{1}{0}{1}".format(a,b))


# 7)Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
#
# non_start('Hello', 'There') ? 'ellohere'
# non_start('java', 'code') ? 'avaode'
# non_start('shotl', 'java') ? 'hotlava'

# Answer
# a,b = ('Hello', 'There')
# c,d = (a[1:],b[1:])
# print(c+d)


# 8)Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
#
# left2('Hello') ? 'lloHe'
# left2('java') ? 'vaja'
# left2('Hi') ? 'Hi'


# Answer
# string = ("Hello")
# first_half = string[0:-2]
# second_half =  string[-2:]
# reversed_string = second_half[::-1]
# # String[0:-2]+
# print("{0}{1}".format(first_half, reversed_string))