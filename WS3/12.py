# Write an algorithm that given  two lists by the user says  if they have a  common element or not.

#We're using ListInput.py


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