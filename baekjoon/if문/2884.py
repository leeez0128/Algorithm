import sys
input = sys.stdin.readline


def solution(H, M):
    if(M > 44):
        print(H, M-45)
    elif(M < 45 and H > 0):
        print(H-1, 60+(M-45))
    elif(M < 45 and H == 0):
        print(23, 60+(M-45))


if __name__ == '__main__':
    H, M = map(int, input().strip().split())
    solution(H, M)
