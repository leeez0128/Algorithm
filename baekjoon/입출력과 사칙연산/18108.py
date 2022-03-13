import sys
input = sys.stdin.readline


def solution(y):
    # 불기 연도를 서기 연도로 변환
    print(y-543)


if __name__ == '__main__':
    y = int(input().strip())
    solution(y)
