init=int(input("Give a number between -10 and 10 "))
i=0

while init>10 or init<-10:
    init=int(input("Give a number between -10 and 10 "))
    if init>10:
        print("Too high")
        i+=1
    elif init<-10:
        i+=1
        print("Too low")
        

print(f"Wrong {i} times")