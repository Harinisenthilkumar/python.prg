per = int(input("Your attendance percentage: "))
if per >= 75:
    print("You're allowed to write exams")
elif per <= 75 and per >= 65:
    med = input("Do you have medical cause? ( Yes/ Noo): ")
    if med == 'Yes' or med == 'yes':
        print("You're allowed to write exams")
    else:
        print("You're not allowed to write exams")
else:
    print("You're not allowed to write exams")
