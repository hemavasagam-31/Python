numbers = [10, 20, 30, 40, 50]
print(numbers[2])

numbers.append(60)
numbers.remove(20)
print(numbers)

values = [3, 14, 8, 22, 9]
print("Largest:", max(values))

items = [1, 2, 2, 3, 4, 4, 5]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)
