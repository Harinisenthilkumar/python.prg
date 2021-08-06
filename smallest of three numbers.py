a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b) and (c > b):
    print("\nSmallest number =",b)
elif ( b > a ) and ( c > a ):
    print("\nSmallest number =",a)
elif ( a > c ) and ( b > c ):
    print("\nSmallest number =",c)
elif a == b and b == c:
    print("\nAll numbers are Equal")
else:
    print("\nSome numbers are equal")
