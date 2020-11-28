temp = input()
m = int(temp)
n = 0
while m != 1:
    if m % 2 == 0:
        m /= 2
    else:
        m = (3 * m + 1) / 2
    n = n + 1
print(n)
