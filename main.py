# 🚨 Don't change the code below 👇
tot=0
number_of_students = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  tot=tot + student_heights[n]
 print(f"total height i= {tot}")
  

for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
  
avg=tot/number_of_students
print(round(avg))






