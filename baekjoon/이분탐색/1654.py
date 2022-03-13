import sys
input = sys.stdin.readline


def solution(K, N, already):
    high, low = sum(already)//N, 1
    while low <= high:
        mid = (high + low) // 2
        cnt = sum([element//mid for element in already])
        if cnt < N:
            high = mid - 1
        elif cnt >= N:
            low = mid + 1
            result = mid
    
    print(result)


if __name__ == '__main__':
    K, N = map(int, input().strip().split())
    already = [int(input().strip()) for _ in range(K)]
    solution(K, N, already)
