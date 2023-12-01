# Write an algorithm that given  two lists by the user says  if they have a  common element or not.

#We're using functions.py
from functions import *


newList1=askList()
newList2=askList()

#Now we want to check if lists have a common element (by creating a flag)

flag=False

for elementList1 in newList1:
    for elementList2 in newList2:
        if(elementList1 == elementList2): 
            flag=True
            break # Stop the inner loop once a common element is found
    if flag:
        break # Stop the outer loop once a common element is found

if flag:
    print("Common elements")
else:
    print("No common element")