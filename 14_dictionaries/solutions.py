book = {"title": "Python Basics", "author": "Sam", "price": 299}
print(book.keys())
print(book.values())

word = "banana"
frequency = {}
for ch in word:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)
