message = "keep learning"
print(message.upper())

word = "coding"
print(word[0], word[-1])

word2 = "education"
vowels = "aeiou"
count = 0
for ch in word2:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

text = "python"
print(text[::-1])
