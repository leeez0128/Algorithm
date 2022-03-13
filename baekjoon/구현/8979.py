import sys
input = sys.stdin.readline


def solution(N, K, countries):
    rank = 1
    for i in range(1, N+1):
        if countries[K][0] < countries[i][0]:
            rank += 1
        elif countries[K][0] == countries[i][0]:
            if countries[K][1] < countries[i][1]:
                rank += 1
            elif countries[K][1] == countries[i][1]:
                if countries[K][2] < countries[i][2]:
                    rank +=1 
    
    print(rank)


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    countries = [[] for _ in range(N+1)]
    for _ in range(N):
        country, gold, silver, bronze = map(int, input().strip().split())
        countries[country] = [gold, silver, bronze]
    solution(N, K, countries)
