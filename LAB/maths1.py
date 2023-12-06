def absolute_value(number: float) -> float:
    """This function will give you the absolute value of any number in R"""

    if number>=0:
        return number
    elif number<0:
        return -number

def max_power_of_two(number: int) -> int:
    """This function will return the highest power of two that divides the given number."""
    flag=True
    
    #Using while and a flag.