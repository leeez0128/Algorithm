import sys
input = sys.stdin.readline


def solution(N, M, broken_buttons):
    min_count = abs(100 - N)

    for nums in range(1000001):
        for num in str(nums):
            if int(num) in broken_buttons:
                break
        else:
            min_count = min(min_count, abs(nums - N) + len(str(nums)))

    print(min_count)


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    broken_buttons = []
    if M != 0:
        broken_buttons = list(map(int, input().strip().split()))
    solution(N, M, broken_buttons)
