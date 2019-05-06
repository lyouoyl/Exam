num3 = 0
for num in range(1,1000):
    if(num % 3 == 0):
        num3 += num

num5 = 0
for num in range(1,1000):
    if(num % 5 == 0):
        num5 += num

num15 = 0
for num in range(1,1000):
    if(num % 15 == 0):
        num15 += num

total = num3 + num5 - num15
print(total)
