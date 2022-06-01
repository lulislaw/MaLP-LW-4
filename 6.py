def super_num(a):
    dela = []
    for i in range(1,a):
        if(a % i) == 0:
            dela.append(i)
    if sum(dela) == a:
        print(a, "true")

for i in range(10001):
    super_num(i)