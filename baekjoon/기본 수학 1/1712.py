import sys
input = sys.stdin.readline


def solution(A, B, C):
    # C*n - ( A + B*n ) > 0
    # (C-B)*n - A > 0
    # n > A // (C-B)
    if (C-B) != 0:
        bep = A // (C-B) + 1
        if bep> 0:
            print(bep)
            return
    print(-1)


if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    solution(A, B, C)
