# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_value = student_scores[0]

for zahl in student_scores:
  if zahl > highest_value:
    highest_value = zahl

print(highest_value)