from math import sqrt

a, b, c = input("podaj a, b, c").split()
a, b, c = int(a), int(b), int(c)

delta = (b ** 2 - 4 * a * c)
print(delta)
roots = []

if delta > 0:
    roots.append((-b - sqrt(delta)) / (2 * a))
    roots.append((-b + sqrt(delta)) / (2 * a))
if delta == 0:
    roots.append((-b) / (2 * a))
if delta < 0:
    print("There are no roots")

print(roots)
