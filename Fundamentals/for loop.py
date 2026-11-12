# Multiplication table
# Input a number and print its multiplication table from 1 to 10.

num=int(input())
for i in range(1, 11):
  print(f"{num} X {i} = {num*i}")