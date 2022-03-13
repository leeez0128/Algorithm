import sys
from itertools import combinations
input = sys.stdin.readline


def solution(card, M):
    answer = 0
    for i in list(combinations(card, 3)):
        if answer < sum(i) <= M:
            answer = sum(i)
      
    print(answer)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    card = list(map(int, input().strip().split()))
    solution(card, M)
