# Eligibility checker
# Ask for a person's age and whether they have an ID. Allow entry only if age is at least 18 and they have an ID.

age=int(input())
id=input().strip().lower()
if(age>=18):
  if(id=="yes"):
    print("Eligible")
  else:
    print("please Register ID")
else:
  print("Not Eligible")