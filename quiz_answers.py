

name = "Dave"

print(f"Hello, {name}")
print("Hello, {}!".format(name))
print("Hello, " + name + "!")


# --------2-----------
m = 1
x = 2
b = 3
y = m * x + b
print(f"When x is {x}, y is {y}")


# ----3-----
length = 2
width = 3
area = length * width
perimeter = length * 2 + width * 2
print(f"Area: {area}, Perimeter: {perimeter}")

# ------4--------
people = 2
avg_slices = 3
slices_per_pizza = 8
slices_needed = people * avg_slices
pizzas_needed = slices_needed / slices_per_pizza
print(f"You need {pizzas_needed} pizzas")
