import sys
input = sys.stdin.readline


def solution(N, M, tree):
    high, low, result = max(tree), 1, 0
    while low <= high:
        mid = (high + low) // 2
        takeout = 0
        for element in tree:
            if element >= mid:
                takeout += element-mid
        if takeout < M:
            high = mid - 1
        elif takeout >= M:
            low = mid + 1
            result = mid
    
    print(result)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    tree = list(map(int, input().strip().split()))
    solution(N, M, tree)