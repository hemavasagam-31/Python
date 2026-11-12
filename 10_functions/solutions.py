def square(n):
    return n * n

def is_even(n):
    return n % 2 == 0

def largest(a, b, c):
    return max(a, b, c)

def count_words(sentence):
    words = sentence.split()
    return len(words)

print(square(6))
print(is_even(11))
print(largest(4, 19, 7))
print(count_words("Python is fun to learn"))
