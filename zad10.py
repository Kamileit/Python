from functools import reduce

a = [1,2,12,4]
b = [2,4,2,8]
a_b = []

for i in range(len(a)):
    a_b.append(a[i] * b[i])

print(reduce(lambda x,y: x+y, a_b))





