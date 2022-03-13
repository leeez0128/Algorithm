import sys
input = sys.stdin.readline


def solution(data):
    print(max(data), data.index(max(data))+1)
        

if __name__ == '__main__':
    data = [int(input().strip()) for _ in range(9)]
    solution(data)
