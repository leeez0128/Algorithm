import sys
input = sys.stdin.readline


def solution(X):
    set_X = set(X)
    sorted_X = sorted(set_X)
    dict_X = dict()
    for i in range(len(sorted_X)):
        dict_X[sorted_X[i]] = i
    for x in X:
        print(dict_X[x], end=" ")


if __name__ == '__main__':
    N = int(input().strip())
    X = list(map(int, input().strip().split()))
    solution(X)
