
height=int(input("enter height"))
bill=0

if height>120:
    age=int(input("enter age"))
    if age<12:
        bill=5
        print("tickets are for $5")
    elif age<18:
        bill=7
        print("tickets are for $7")
    elif age>=18:
        bill=12
        print("tickets are for $12")
    photo=input("do you want photograph Y or N")
    if photo=="Y" or photo=="y":
        bill+=3
        print("extra $3 for the same")
    else:
        print("okay!")
    print(f"your final bill is ${bill}")
else:
    print("can't Ride")
