#Same as 13, this time we use a variable i, to which we add 1.
#Using functions.py

from functions import askList

newList1=askList()
newList2=askList()

#Now we want to check if lists have a common element (by creating a flag)

i=0 #Variable to count the number of elements

for elementList1 in newList1:
    for elementList2 in newList2:
        if(elementList1 == elementList2): 
            i+=1
        else:
            i+=0

print(f"{i} common element(s)")
