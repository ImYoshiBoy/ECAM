#This one is a bit harder
#Let's start by asking  lists 

from functions import *

newList1=askList()
newList2=askList()

#For this one we will use a function, dont ask why, i want to.

common_elements, occurrences_list1, occurrences_list2 = find_common_elements(newList1, newList2)

# Display results
print("\nCommon Elements:", common_elements)
print("Occurrences in List 1:", occurrences_list1)
print("Occurrences in List 2:", occurrences_list2)
