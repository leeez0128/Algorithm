import sys
input = sys.stdin.readline


def solution(x, y):
    if(x < 0 and y < 0):
        print(3)
    elif(x < 0 and y > 0):
        print(2)
    elif(x > 0 and y > 0):
        print(1)
    elif(x > 0 and y < 0):
        print(4)


if __name__ == '__main__':
    x = int(input().strip())
    y = int(input().strip())
    solution(x, y)
