import sys
input = sys.stdin.readline


def solution(H, W, N):
    X = N // H + 1 # 2
    Y = N % H # 4
    if Y == 0:
        Y = H
        X -= 1
    if len(str(X)) == 1:
        X = '0' + str(X)
    print(Y, X, sep="")


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        H, W, N = map(int, input().strip().split())
        solution(H, W, N)
