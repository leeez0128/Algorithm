import sys
input = sys.stdin.readline


def solution(A, B):
    print(A*int(B[2]), A*int(B[1]), A*int(B[0]), A*int(B), sep="\n")


if __name__ == '__main__':
    A = int(input().strip())
    B = input().strip()
    solution(A, B)
