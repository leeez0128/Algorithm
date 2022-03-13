import sys
input = sys.stdin.readline


def solution(numbers):
    sosu = 0
    for num in numbers:
        if num == 1: continue
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            sosu += 1
    print(sosu)


if __name__ == '__main__':
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    solution(numbers)