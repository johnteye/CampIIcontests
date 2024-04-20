t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    res = sum(arr)
    even, odd = 0, 0
    even_sum , odd_sum = 0, 0
    for val in arr:
        if val % 2 == 0:
            even += 1
            even_sum = val
        else:
            odd_sum = val
            odd += 1

    for i in range(q):
        curr = list(map(int, input().split()))
        if curr[0] == 0:
            for op in curr[1:]:
                if (odd_sum) % 2 == 0:
                    odd_sum += op
                    res += (op * odd)
                if even_sum % 2 == 0:
                    res += (op * even)
                    even_sum += op
                    print(res)
                else:
                    print(res)
        else:
            for op in curr[1:]:
                if (even_sum) % 2 == 1:
                    even_sum += op
                    res += (op * even)
                if odd_sum % 2 == 1:
                    res += (op * odd)
                    odd_sum += op
                    print(res)
                else:
                    print(res)

    #       ans = sum(nums)
    # for i in range(q):
    #     j, num = map(int, input().split())
    #     if j == 0:
    #         ans += num * even
    #         if num%2 == 1:
    #             odd += even
    #             even = 0
    #     else:
    #         ans += num * odd
    #         if num%2 == 1:
    #             even += odd
    #             odd = 0
    #     print(ans)
        # print(odd_sum, even_sum)

    

