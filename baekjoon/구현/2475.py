import sys
input = sys.stdin.readline


def solution(serial):
    result = 0
    for num in serial:
        result += num ** 2
    print(result % 10)
    

if __name__ == '__main__':
    serial = list(map(int, input().strip().split()))
    solution(serial)
