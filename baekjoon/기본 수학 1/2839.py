import sys
input = sys.stdin.readline


def solution(N):
    if N % 5 == 0:
        print(N//5)
        return
    else:
        for i in range(1, N//3 + 1):
            if (N - 3*i) % 5 == 0:
                print(i + (N-3*i)//5)
                return
    print(-1)


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)