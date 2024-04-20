n = 10
if n <= 1:
    print(0)
    exit()
prime= [1 for i in range(n+1)]
prime[0], prime[1] = 0, 0

for i in range(2, n+1):
    if not prime[i]:
        continue
    for j in range(i+i, n+1, i):
        if j%i == 0:
            prime[j] = 0
print(prime)

