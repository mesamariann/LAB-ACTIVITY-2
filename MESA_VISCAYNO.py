# Prompt the user to input full name
name1 = str(input("Enter your full name: "))

num = eval(input("Enter your ID number: "))

course1 = str(input("Enter your course: "))

sec1 = str(input("Enter your section: "))

grade1 = eval(input("Enter your grade for the first quarter grade: "))
grade2 = eval(input("Enter your grade for the second quarter grade :"))
grade3 = eval(input("Enter your grade for the third quarter grade: "))
grade4 = eval(input("Enter your grade for the fourth quarter grade: "))

average = (grade1 + grade2 + grade3 + grade4) / 4
print("The average of your grades is " + str(average))