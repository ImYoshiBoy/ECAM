#This one is a bit harder
#Let's start by asking  lists 

size1=input("Give a size:\n")
newList1=[]

for i in range(int(size1)):
    element=input("Give an element to push into the list:\n")
    newList1.append(element)

print(f"Here is the first list! {newList1}")

size2=input("Give a size:\n")
newList2=[]

for i in range(int(size2)):
    element=input("Give an element to push into the list:\n")
    newList2.append(element)

print(f"Here is the first list! {newList2}")

#For this one we will use a function, dont ask why, i want to.

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

common_elements, occurrences_list1, occurrences_list2 = find_common_elements(newList1, newList2) #

# Display results
print("\nCommon Elements:", common_elements)
print("Occurrences in List 1:", occurrences_list1)
print("Occurrences in List 2:", occurrences_list2)
