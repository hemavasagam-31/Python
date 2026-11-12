# Simple menu calculator
# Display options for addition, subtraction, multiplication and division. Ask the user to select one and enter two numbers.

num1=int(input())
num2=int(input())
us=int(input())
if(us==1):
  print(f"1.Add {num1+num2}")
elif(us==2):
  print(f"2.Sub {num1-num2}")
elif(us==3):
  print(f"3.Mul {num1*num2}")
elif(us==4):
  print(f"4.Div {num1/num2}")
  