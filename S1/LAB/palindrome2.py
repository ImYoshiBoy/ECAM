#Method 2  
def palindrome(word:str) -> str or bool:
    """This function is cool. Will tell if u're word is a palindrome."""

    if len(word)==0:
        return "Where word?? Please insert a word." #We condsider empty strings. We bully the user. 
    
    n=len(word)
    k=0
    result=True

    while result and k <= n//2:
        result=word[k]==word[n-1-k] #compares the character at index k with the character at the symmetric position from the end of the word
        k+=1
    return result