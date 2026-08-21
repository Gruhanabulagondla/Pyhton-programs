name = input("Enter student name: ")

m1 = float(input("Enter Python marks: "))
m2 = float(input("Enter DBMS marks: "))
m3 = float(input("Enter Java marks: "))
m4 = float(input("Enter HTML marks: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")