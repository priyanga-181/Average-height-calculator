# 🚨 Don't change the code below 👇
tot=0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  tot=tot + student_heights[n]
avg=tot/len(student_heights)
print(round(avg))


# 🚨 Don't change the code above 👆



#Write your code below this row 👇




