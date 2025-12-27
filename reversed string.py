def reversed_string(s):
    rev = ""
    for char in s:
        rev =char+s
        return rev
    text = "hello"
    print(reversed_string(text))  # Output should be "olleh"