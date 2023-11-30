#Same as 13, this time we use a variable i, to which we add 1.

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

#Now we want to check if lists have a common element (by creating a flag)

i=0 #Variable to count the number of elements

for elementList1 in newList1:
    for elementList2 in newList2:
        if(elementList1 == elementList2): 
            i+=1
        else:
            i+=0

print(f"{i} common element(s)")
