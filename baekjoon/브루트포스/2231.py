import sys
input = sys.stdin.readline


def solution(N):
    result = -1
    for i in range(N):
        length = len(str(i))
        hab = i
        for j in range(length):
            hab += int(str(i)[j])
        if hab == N:
            result = i
            break
    if result == -1:
        print(0)
    else:
        print(result)


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)