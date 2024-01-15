#!/usrbin/python3
"""Defining append after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file
    Args: filename, search_string, new_string
    """
    text = ""
    with open(filename, mode="r", encoding='utf-8') as fp:
        lines = fp.readlines()
    for line in lines:
        if line.find(search_string) != -1:
            text += line + new_string
        else:
            text += line
    with open(filename, mode="w", encoding='utf-8') as fp:
        fp.write(text)