#!/usr/bin/python3
"""
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Prototype is: def text_indentation(text):

    text must be string, else 
    raise TypeError exception with the message text must be a string
    No space at the beginning or at end of printed line
"""

def text_indentation(text):
    """
        insert doble jump line after . : or ?
    """
    str_error = "text must be a string"
    new_text = ""
    flag = False
    if type(text) is not str:
        raise TypeError(str_error)
    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")
    for char in new_text:
        if char in [".", "?", ":"]:
            print(char)
            print()
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False