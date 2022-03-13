import sys
input = sys.stdin.readline


def solution(N, sangguen, M, find):
    sangguen = sorted(sangguen)
    result = dict()
    for x in sangguen:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    
    for x in find:
        if x in result:
            print(result[x], end=' ')
        else:
            print(0, end=' ')
        

if __name__ == '__main__':
    N = int(input().strip())
    sangguen = list(map(int, input().strip().split()))
    M = int(input().strip())
    find = list(map(int, input().strip().split()))
    solution(N, sangguen, M, find)
