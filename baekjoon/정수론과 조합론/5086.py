import sys
input = sys.stdin.readline


def solution(num1, num2):
    if num2 % num1 == 0:
        print("factor")
        return
    elif num1 % num2 == 0:
        print("multiple")
        return
    else:
        print("neither")
        return


if __name__ == '__main__':
    while True:
        num1, num2 = map(int, input().strip().split())
        if num1 == 0 and num2 == 0:
            break
        solution(num1, num2)
