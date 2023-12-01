#Same as 13, this time we use a variable i, to which we add 1.
from functions import *

newList1=askList() #Here, im calling the function askList(), which is defined in the functions.py file. 
#If you want to replace this line, delete this one and write that down:
# size=input("Give a size:\n")
#     newList=[]

#     for i in range(int(size)):
#         element=input("Give an element to push into the list:\n")
#         newList.append(element)

#print(newList). The name of your variable will now be newList. You can create many of them, just replace newList by another name.
newList2=askList() 

#Now we want to check if lists have a common element (by creating a flag)

i=0 #Variable to count the number of elements

for elementList1 in newList1:
    for elementList2 in newList2:
        if(elementList1 == elementList2): 
            i+=1

print(f"{i} common element(s)")
