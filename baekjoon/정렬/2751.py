import sys
input = sys.stdin.readline


def solution(numbers):
    numbers.sort()
    for number in numbers:
        print(number)


if __name__ == '__main__':
    N = int(input().strip())
    numbers = [int(input().strip()) for _ in range(N)]
    solution(numbers)
