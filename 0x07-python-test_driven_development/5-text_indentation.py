#!/usr/bin/python3
"""A text-Indentation Module

Parameters:
    text (str) text to trunicate and search for characters
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Raise:
        TypeError
    Return:
        void
    """
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
