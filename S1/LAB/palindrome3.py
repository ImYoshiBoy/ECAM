#Working with a sentence is working with a string, without sapce and punctuation.

#Let's work with the palindrome2.py function, with a few edits.

#I allow myself to use .replace(). We could do it manually with a really short piece of code:
# my_string = "string "
# old_substring = "i"
# new_substring = "o"
  
# split_list = my_string.split(old_substring) 
# new_list = [new_substring if i < len(split_list)-1 else '' for i in range(len(split_list)-1)] 
# new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list)-1)] + [split_list[-1]]) 
  
# print(new_string) 

def sentence_palindrome(sentence:str) -> str or bool:
    """This is a really crazy function that will check if yout SENTENCE is a palindrome????? Insane!"""
    sentence=sentence.lower()
    if len(sentence)==0:
        return "Where sentence?? Please insert a sentence." #We condsider empty strings. We bully the user. 
    


    punctuation = '''!()-[];:'",<>./?@#$%^&*_~'''
    # Removing punctuations in string using a cool loop
    #Deleting the spaces, creating a new variable to make stuff clear for myself.
    for element in sentence:
        if element in punctuation:
            sentence = sentence.replace(element, "")
    sentence=sentence.replace(" ", "")


    n=len(sentence)
    k=0
    result=True
    while result and k <= n//2:
        result=sentence[k]==sentence[n-1-k] #compares the character at index k with the character at the symmetric position from the end of the word
        k+=1
    return result