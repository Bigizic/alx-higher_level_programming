#!/usr/bin/python3
"""Text Indentation Module
a function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        try:
            raise TypeError("text must be a string")
        except Exception:
            raise TypeError("text must be a string")
    else:
        space = False
        for letters in text:
            if space and letters == ' ':
                continue
            if letters in ['.', '?', ':']:
                print(letters, end="")
                print()
                print()
                space = True
            else:
                print(letters, end="")
                space = False
