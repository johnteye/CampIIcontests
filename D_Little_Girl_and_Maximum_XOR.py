n , m = map(int, input().split())
res = n ^ m

print(2 ** res.bit_length() - 1)
