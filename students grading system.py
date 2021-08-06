def  getinput ():
    gradeinput = int(input("\nEnter your Grade : "))
    if gradeinput == 10:
        print("\nYour Grade: A+")
    elif gradeinput== 9:
        print("\nYour Grade: A ")
    elif gradeinput == 8:
        print("\nYour Grade: B+ ")
    elif gradeinput == 7:
        print("\nYour Grade: B ")
    elif gradeinput == 6:
        print("\nYour Grade: C ")
    elif gradeinput <=5 and gradeInput > -1:
        print("\nYour Grade:(Fail)")
    elif gradeinput<0:
        print("\nYour input is less than 0\nEnter Correct Grade ")
        getinput()
    else:
        print("\nYour input is higher than 10\nEnter Correct Grade ")
        getinput()
getinput()
