def sums(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

maxi = 2 * (10 ** 5) + 1 

pre_sum = [0]

for i in range(1, maxi):

    num = sums(i)

    pre_sum.append(pre_sum[i - 1] + num)

t = int(input())
for _ in range(t):
    n = int(input())
    print(pre_sum[n])