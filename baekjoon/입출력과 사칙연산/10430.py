import sys
input = sys.stdin.readline


def solution(A, B, C):
    print((A+B) % C, ((A % C)+(B % C)) % C, sep="\n")
    print((A*B) % C, ((A % C)*(B % C)) % C, sep="\n")


if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    solution(A, B, C)
