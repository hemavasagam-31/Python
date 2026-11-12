colors = ("red", "blue", "green", "yellow")
print(colors[1])

# Tuples are immutable. Uncommenting below will raise TypeError.
# colors[0] = "black"

length_width = (8, 5)
length, width = length_width
print("Area:", length * width)
