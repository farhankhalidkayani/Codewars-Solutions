# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    
    return name + " plays banjo" if name[0].lower()=='r' else name + " does not play banjo"