# Prime number checker
# Determine whether an integer greater than 1 is prime.

num=int(input())
if(num>1):
  for i in range(2, num+1):
    if(num%2==0):
      print("Not prime")
      break
  else:
      print("prime")
else:
  print("Not Prime")