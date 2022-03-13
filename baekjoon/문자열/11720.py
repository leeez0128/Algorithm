import sys
input = sys.stdin.readline


def solution(N, number):
    result = 0

    for i in range(N):
        result += int(number[i])
    
    print(result)


if __name__ == '__main__':
    N = int(input().strip())
    number = input().strip()
    solution(N, number)
