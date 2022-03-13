import sys
input = sys.stdin.readline


def solution(R1, S):
    print(S*2 - R1)


if __name__ == '__main__':
    R1, S = map(int, input().strip().split())
    solution(R1, S)
    