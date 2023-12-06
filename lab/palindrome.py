#Method

def equality(string1:str, string2: str) -> str or bool:
    """Very usefull function. Will tell you if 2 strings are equal."""

    if len(string1) == 0 or len(string2) == 0:
        return "You need to enter an actual character, empty string is not one. Example of a character: 'W'"

    return string1==string2

def symmetrical(super_string:str) -> str or bool:
    """Will reverse your word :o magic. Many ways to do it. Slicing, loops, reverse()... I will use loop for this one, since slicing is illegal."""

    if len(super_string)==0:
        return "You need to enter an actual character, empty string is not one. Example of a character: 'W'"
    #Slicing:
    #return super_string[::1]
    result=""
    for char in super_string:
        result = char + result #and PLEASE not result + char. Wasted 10 mins on this.
    return result

def is_palindrome(omega_string:str) ->  str or bool:
    """Will tell you wether the word you enter is a palindrome or not"""

    if len(omega_string)==0:
        return "This is kind of an empty string. I dont know. U can read nothing from left to right and right to left. Who knows..."
    
    return equality(omega_string, symmetrical(omega_string)) #Nice
