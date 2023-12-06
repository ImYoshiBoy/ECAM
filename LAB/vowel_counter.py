def is_vowel(vowel:str) -> str:
    """Will tell you if the first caracter you entered is a vowel or not"""
    vowels=["a","e","i","o","u","y"]
    arg = []
#lmao why is this not wroking

    if not len(vowel) == 1:
        a=3

    

    if len(vowel) == 0:
        return False
    elif vowel.lower() in vowels:
        return True
    elif not (vowel.lower() in vowels):
        return False