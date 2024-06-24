# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    reversed_text = ""
    word = ""
    
    for char in text:
        if char != " ":
            word += char  # Build the current word
        else:
            reversed_text += word[::-1] + " "  # Add the reversed word and the space
            word = ""  # Reset the current word

    reversed_text += word[::-1]  # Add the last word (if any) after the loop
    
    return reversed_text
