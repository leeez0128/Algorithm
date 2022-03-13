import sys
input = sys.stdin.readline


def solution(yaksu):
    yaksu = sorted(yaksu)
    print(yaksu[0]*yaksu[-1])


if __name__ == '__main__':
    _ = int(input().strip())
    yaksu = list(map(int, input().strip().split()))
    solution(yaksu)
