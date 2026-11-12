for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

nums = [2, 3, 4, 7, 10, 11]
even_count = 0
for n in nums:
    if n % 2 == 0:
        even_count += 1
print("Even count:", even_count)
