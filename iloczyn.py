a = [1, 2, 12, 4]
b = [2, 4, 2, 8]


def scalar_sum(a, b):
    akumulator = 0
    for v1, v2 in zip(a, b):
        akumulator += v1 * v2
    return akumulator


# akumulator = scalar_sum(a, b)
#
# print(akumulator)
