def absolute_value(number: float or int) -> float or int:
    """This function will give you the absolute value of any number in R"""

    if number>=0:
        return number
    elif number<0:
        return -number

def max_power_of_two(number: int) -> int:
    """This function will return the highest power of two that divides a given number."""

    if number<=0:
        #raise ValueError("Input must be a positive integer.") 
        #Just stoping the code, that is not what I want.
        return "Input must be a positive integer."
    else:
        result = 0
        while number % 2 == 0:
            number = number/2  # This lign is equivalent to number>>=1 (didnt know)
            result +=1
    return result
        
    #Using while and a flag.