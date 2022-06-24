"""write a python program to add 'ing' at the end of a given string
(length should be at least 3). if the given string already ends with 'ing' then add 'ly' instead.
if the string length of the given string is less than 3, leave it unchanged.
example:- sample string : 'abc' expected result : 'abcing' sample string : 'string' expected result : 'stringly'"""

string = 'string'

"""check if the string is bigger or equal than 3'"""
if len(string) >= 3:
    if string.endswith('ing'):
        """add 'ly' at the end'"""
        string = string + 'ly'
    else:
        """add 'ing' at the end'"""
        string = string + 'ing'

print(string)