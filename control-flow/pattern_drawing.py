length = int(input("Enter the size of the pattern: "))
x = 0 
y = 0
while x < length:
    for y in range(length):
        print("*",end="")
    x=x+1
    print("")
    