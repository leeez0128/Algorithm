import sys
input = sys.stdin.readline


def solution(a, b):
    repeat = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
    
    a = int(str(a)[-1])
    if a != 0:
        print(repeat[a][b % len(repeat[a])])
    else:
        print(10)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        a, b = map(int, input().strip().split())
        solution(a, b)