# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    return True if text[(len(text)-1)-(len(ending)-1):len(text)]==ending else False