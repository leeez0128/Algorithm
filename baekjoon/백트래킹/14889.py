import sys
from itertools import combinations
input = sys.stdin.readline


def solution(N, startlink):
    result = 1e9
    people = [i for i in range(N)]
    every_com = combinations(people, N//2)
    
    for start_team in every_com:
        start_sum, link_sum = 0, 0
        link_team = list(set(people) - set(start_team))
        for start in combinations(start_team, 2):
            start_sum = start_sum + startlink[start[0]][start[1]] + startlink[start[1]][start[0]]
        for link in combinations(link_team, 2):
            link_sum = link_sum + startlink[link[0]][link[1]] + startlink[link[1]][link[0]]
        result = min(result, abs(start_sum - link_sum))
    print(result)


if __name__ == '__main__':
    N = int(input().strip())
    startlink = [list(map(int, input().strip().split())) for _ in range(N)]
    solution(N, startlink)
