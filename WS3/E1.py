from functions import *

size=input("Give a size:\n")
newList=[]

for i in range(int(size)):
    element=input("Give an element to push into the list:\n")
    newList.append(element)

compared_element=int(newList[0])

flag=False
j=1

while j<len(newList) and not flag:
    if compared_element>int(newList[j]):
        flag=True
        print(flag)
        print("Not sorted.")

    j+=1

print("Sorted")