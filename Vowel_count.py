"""Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""


def get_count(sentence):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in list(sentence):
        for j in vowels:
            if i == j:
                counter = counter + 1

    return counter



print(get_count('Hallo'))

