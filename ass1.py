
# Question1

P = int(input("Enter First number  : "))
Q = int(input("Enter Second number : " ))
R = int(input("Enter Third number :" ))
S= P + Q + R
average = S/3
print("Average of the three numbers : ", average )

# Question2

G_I = int(input("Enter The Gross Income : "))
D = int(input(" Enter Dependent : "))
S_D = 10000
D_D = 3000
D_I = D_D*D
Taxable_Income = G_I - S_D - D_I
Tax = float((20 / 100) * (Taxable_Income))
print("Your Income Tax : ", Tax)

# Question3

SID = input("Enter Student's SID : ")
Name = input("Enter Student's Name : ")
Gender = input("Enter Student's Gender : ")
Course_Name = input("Name of the Course : ")
CGPA = input("CGPA of the Student : ")
student = [SID,Name,Gender,Course_Name,CGPA ]
print(student)

# Question4

A = int(input("Marks of Student A : "))
B = int(input("Marks of Student B : "))
C = int(input("Marks of Student C : "))
D = int(input("Marks of Student D : "))
E = int(input("Marks of Student E : "))
list = [A,B,C,D,E]
print(list)

# question 5a

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)

# question 5b

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color[3:5]=['Purple','Purple']
print(color)
