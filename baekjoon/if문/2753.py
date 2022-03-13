import sys
input = sys.stdin.readline


def solution(year):
    if((year % 4) == 0):
        if((year % 100) != 0 or (year % 400) == 0):
            print('1')
            return
    print('0')


if __name__ == '__main__':
    year = int(input().strip())
    solution(year)
