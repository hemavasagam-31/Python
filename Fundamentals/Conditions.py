# Grade calculator
# Accept a score from 0 to 100. Assign grades: A for 90–100, B for 75–89, C for 60–74, D for 40–59, F below 40. Reject invalid scores.

mark=int(input())
if(mark>0 and mark<=100):
  if(mark >=90 and mark<=100):
    print("Grade:A")
  elif(mark >=75 and mark<=89):
    print("Grade:B")
  elif(mark >=60 and mark<=74):
    print("Grade:C")
  elif(mark >=40 and mark<=59):
    print("Grade:D")
  else:
    print("Grade:F")
else:
  print("Invalid")