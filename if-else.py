name=input("enter a name:")
exp=int(input(f"enter {name} experience:"))
if exp>1:
    if exp>=1 and exp<=5:
        print("salary is 25k")
    elif exp>=6 and exp<=10:
        print("salary is 50k")
    else:
        print("salary is 75k")
else:
    print("not allowed")