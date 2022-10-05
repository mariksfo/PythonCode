totalClasses = int(input("Enter the total number of classes  "))
attendedClasses = int(input("Enter the number of attended classes  "))

percentage = (attendedClasses/totalClasses) + 100

if percentage < 75:
    cause = input("Was abscense because of a Medical case, Y/N?")

    if cause.lower() == "y":
        print("The student is allowed to sit in exams")
    else:
        print("Sorry you are not allowed to sit in exams ")
        print("Its because you have only attended {} classes".format(percentage))

else:
    print("Student is allowed to sit in exams")
    print("He attended {} class".format(percentage))