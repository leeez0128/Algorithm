import sys
input = sys.stdin.readline


def solution(N, C, houses):
    high, low, result = houses[-1]-houses[0], 1, 0
    while low <= high:
        mid = (high + low) // 2
        cnt = 1
        from_ = houses[0]
        for i in range(1, N):
            if houses[i] >= from_ + mid:
                cnt += 1
                from_ = houses[i]
        if cnt < C:
            high = mid - 1
        elif cnt >= C:
            low = mid + 1
            result = mid
    
    print(result)


if __name__ == '__main__':
    N, C = map(int, input().strip().split())
    houses = sorted([int(input().strip()) for _ in range(N)])
    solution(N, C, houses)
