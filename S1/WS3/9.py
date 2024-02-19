newList=[]
max=int(input("Give the first int"))
flag=False

for i in range(9):
    element=int(input("Give an element to push into the list:\n"))
    newList.append(element)
    if element>max:
        max=element
print("done")#didnt finish that one. correction in class