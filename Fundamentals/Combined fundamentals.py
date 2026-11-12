# Mini student grade report
# Input a student's name and marks in three subjects. Calculate the average and display pass/fail using a pass mark of 35 per subject.

name=input()
m1=int(input())
m2=int(input())
m3=int(input())
if(m1>=35 and m2>=35 and m3>=35):
  avg=(m1+m2+m3)/3
  print("Result: Pass")
else:
  print("Result: Fail")