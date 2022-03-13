import sys
input = sys.stdin.readline


def solution(N):
    insu = 2
    while N != 1:
        if N % insu == 0:
            N /= insu
            print(insu)
        else:
            insu += 1


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
