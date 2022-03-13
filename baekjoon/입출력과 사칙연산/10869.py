import sys
input = sys.stdin.readline


def solution(A, B):
    print(A+B, A-B, A*B, A//B, A%B, sep="\n")


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    solution(A, B)
