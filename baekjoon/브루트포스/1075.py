import sys
input = sys.stdin.readline


def solution(N, F):
    for i in range(100):
        if i < 10:
            change = '0' + str(i)
        else:
            change = str(i)
        newN = int(N[:-2] + change)
        if newN % F == 0:
            print(str(newN)[-2:])
            return


if __name__ == '__main__':
    N = input().strip()
    F = int(input().strip())
    solution(N, F)
