#Gonna create a bunch of functions here. The goal is to call them in differents files, to make the work easier

def askList():
    size=input("Give a size:\n")
    newList=[]

    for i in range(int(size)):
        element=input("Give an element to push into the list:\n")
        newList.append(element)

    return newList