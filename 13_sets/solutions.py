items = ["pen", "pen", "book", "book", "bag"]
unique_items = set(items)
print(unique_items)

colors = {"red", "blue"}
colors.add("green")
colors.remove("blue")
print(colors)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(common)
