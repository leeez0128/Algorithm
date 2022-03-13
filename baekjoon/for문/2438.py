import sys 
input = sys.stdin.readline


def solution(N):
    for i in range(1, N+1):
        for _ in range(i):
            print("*", end="")
        print()


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
