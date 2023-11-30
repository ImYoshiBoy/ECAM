# Write an algorithm that given  two lists by the user says  if they have a  common element or not.

#We're using ListInput.py


size=input("Give a size:\n")
newList1=[]

for i in range(int(size)):
    element=input("Give an element to push into the list:\n")
    newList1.append(element)

print(f"Here is the first list! {newList1}")

size=input("Give a size:\n")
newList2=[]

for i in range(int(size)):
    element=input("Give an element to push into the list:\n")
    newList2.append(element)

print(f"Here is the first list! {newList2}")