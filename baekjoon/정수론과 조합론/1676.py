import sys, math
input = sys.stdin.readline


def solution(N):
    num = str(math.factorial(N))
    zero = 0
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) == 0:
            zero += 1
        else:
            print(zero)
            return


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
