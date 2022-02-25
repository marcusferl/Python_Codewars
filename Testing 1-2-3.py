"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""



def number(lines):
    counter = 1
    new_list =[]
    for _ in lines:
        new_list.append(str(counter) + ': ' + _)
        counter = counter + 1
    return new_list

number(["a", "b", "c"])