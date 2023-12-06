# Write an algorithm that given  two lists by the user says  if they have a  common element or not.

#We're using functions.py
from functions import *


newList1=askList()
newList2=askList()

#Now we want to check if lists have a common element (by creating a flag)
flag=False
i = 0
j = 0

while i < len(newList1) and not flag:
    while j<len(newList2) and not flag:
        if newList1[i] == newList2[j]:
            flag=True
            print(f"COMONON ELEMENTS")
            print(not flag)
        j += 1
    i += 1