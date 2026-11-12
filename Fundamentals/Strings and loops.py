# Count vowels
# Count the vowels in a sentence, ignoring uppercase or lowercase differences.

text=input()
c=0
for ch in text.lower():
  if ch in "aeiou":
    c+=1
print(text, c)