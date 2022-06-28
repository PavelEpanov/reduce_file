from functools import reduce

my_list = list(range(-9, 10))

a = list(filter(lambda x: x % 2 == 0, my_list))
print(my_list)
print(a)

def rem():
    res = []
    for x in my_list:
        if x % 2 == 0:
            res.append(x)
    print(res)

rem()

h = [x for x in my_list if x > 0] # х равен выражению слева
print(h)

###

l = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
k = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print(l)
print(k)

L = [1, 2, 3, 4, 5] # то же самое что и l reduce
res = L[0]
for i in L[1:]:
    res = res + i

print(res)
K = [1, 2, 3, 4, 5] # то же самое что и k reduce
res2 = K[0]
for l in K[1:]:
    res2 = res2 * l

print(res2)

