import sys
input = sys.stdin.readline


def solution(i, A, B):
    print("Case #", i+1, ": ", A, " + ", B, " = ", A+B, sep="")


if __name__ == '__main__':
    T = int(input().strip())
    for i in range(T):
        A, B = map(int, input().strip().split())
        solution(i, A, B)
