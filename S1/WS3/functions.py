#Gonna create a bunch of functions here. The goal is to call them in differents files, to make the work easier

def askList() -> list:
    """This function will return a list, that the user will input."""
    size=input("Give a size:\n")
    newList=[]

    for i in range(int(size)):
        element=input("Give an element to push into the list:\n")
        newList.append(element)

    return newList

#Here i am using a dictionnary.
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
def find_common_elements(list1, list2):
    # Find common elements
    common_elements = set(list1) & set(list2)

    # Count occurrences in each list
    occurrences_list1 = {element: list1.count(element) for element in common_elements} #The count() method returns the number of elements with the specified value.
    occurrences_list2 = {element: list2.count(element) for element in common_elements}

    return common_elements, occurrences_list1, occurrences_list2