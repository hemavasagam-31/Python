# Number guessing game
# Generate a random number from 1 to 20. Let the player guess until correct, providing 'too high' or 'too low' hints.

import random
sn=int(input())
g=0
while g!=sn:
  g=int(input())
  if(g<sn):
    print("low")
  elif(g>sn):
    print("high")
print("Corect!")