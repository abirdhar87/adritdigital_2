val1=int(input("Enter a number: "))
if val1>0:
    if(val1%2==0):
        print(f"{val1} is an even number")
    else:
        print(f"{val1} is an odd number")
else:
    print("Value is zero or less than zero")
