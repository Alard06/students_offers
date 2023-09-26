# covid

def max_social_distance(N, K, seats):
    left = 1
    right = seats[N - 1] - seats[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        count = 1
        start = seats[0]

        for i in range(1, N):
            if seats[i] - start >= mid:
                count += 1
                start = seats[i]

        if count >= K:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


N, K = map(int, input().split())
seats = list(map(int, input().split()))
print(max_social_distance(N, K, seats))
