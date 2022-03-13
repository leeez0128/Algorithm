import sys
input = sys.stdin.readline


def solution(N):
    for i in range(N, 0, -1):
        for _ in range(i-1):
            print(' ', end="")
        for _ in range(N-i+1):
            print("*", end="")
        print()
        

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
