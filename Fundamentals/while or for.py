# Factorial
# Calculate n factorial, where n is a non-negative integer. Treat 0! as 1.

n=int(input())
fact=1
for i in range(1, n+1):
  fact*=i
print(fact)


# n=int(input())
# fact=1

# while(n>0):
#   fact*=n
#   n-=1
# print(fact)