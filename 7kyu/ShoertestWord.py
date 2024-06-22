# // Simple, given a string of words, return the length of the shortest word(s).

# // String will never be empty and you do not need to account for different data types.


def find_short(s):
    words=s.split()
    Min=len(words[0])
    for i in range(1,len(words)):
        curr=len(words[i])
        Min=curr if curr<Min else Min
    return Min