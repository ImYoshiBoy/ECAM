vowels=["a","e","i","o","u","y"]


#I allow myself to use .replace(). We could do it manually with a really short piece of code:
# my_string = "string "
# old_substring = "i"
# new_substring = "o"
  
# split_list = my_string.split(old_substring) 
# new_list = [new_substring if i < len(split_list)-1 else '' for i in range(len(split_list)-1)] 
# new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list)-1)] + [split_list[-1]]) 
  
# print(new_string) 


def is_vowel(vowel:str) -> str:
    """Will tell you if the first caracter you entered is a vowel or not."""

    if len(vowel) == 0:
        return "You need to enter an actual character, empty string is not one. Example of a character: 'W'"

    elif not len(vowel) == 1:
        arg = list(vowel.replace(" ", ""))
        if arg[0].lower() in vowels:
            return True
        else:
            return False
        
    elif vowel.lower() in vowels:
        return True
    
    elif not (vowel.lower() in vowels):
        return False
    
def count_vowels(cool_string: str) -> str:
    """Will count the amount of vowel in a given word/sentence."""
    if len(cool_string) == 0:
        return "You need to enter an actual word or a sentence, empty string is not one. Example of a sentence: 'Hello world!'"
    i=0
    arg = list(cool_string.replace(" ", ""))
    for element in arg:
        if element.lower() in vowels:
            i+=1

    return i