import sys
input = sys.stdin.readline


def solution(A, B):
    print(A + B)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        A, B = map(int, input().strip().split())
        solution(A, B)
