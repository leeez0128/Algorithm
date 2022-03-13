import sys
input = sys.stdin.readline


def solution(X):
    answer = 0
    while X != 0:
        if X % 2 == 1:
            answer += 1
        X //= 2
    print(answer)


if __name__ == '__main__':
    X = int(input().strip())
    solution(X)