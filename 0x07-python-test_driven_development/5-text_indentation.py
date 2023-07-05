#!/usr/bin/python3


"""
    text_indentation - Function
"""


def text_indentation(text):
    """
        Prints text with 2 lines after each of these characters: [., ?, :]
        @text: The text
        Return: No return
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
