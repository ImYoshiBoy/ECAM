vowels=["a","e","i","o","u","y"]


#I allow myself to use .replace(). We could do it manually with a really short piece of code:
# my_string = "string "
# old_substring = "i"
# new_substring = "o"
  
# split_list = my_string.split(old_substring) 
# new_list = [new_substring if i < len(split_list)-1 else '' for i in range(len(split_list)-1)] 
# new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list)-1)] + [split_list[-1]]) 
  
# print(new_string) 

#I hope that it is ok.


def is_vowel(vowel:str) -> bool:
    """Will tell you if the first caracter you entered is a vowel or not."""

    if len(vowel) == 0:
        return "You need to enter an actual character, empty string is not one. Example of a character: 'W'. Please do not enter nothing again. It's wasting my time"

    elif not len(vowel) == 1: 
        arg = list(vowel.replace(" ", ""))

        #I allow myself to use 'element in list'. However, we could use a loop:

        if arg[0].lower() in vowels: #Here I am taking the first vowel so that it still works even tho the user is not inputing correctly.
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
        return "You need to enter an actual word or a sentence, empty string is not one. Example of a sentence: 'Hello world!'. Please do not do this mistake again."
    i=0
    arg = list(cool_string.replace(" ", ""))
    for element in arg:
        if is_vowel(element):
            i+=1

    return i