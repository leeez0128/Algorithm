import sys
input = sys.stdin.readline


def solution(M, N):
    sosu = []
    for num in range(M, N+1):
        if num == 1: continue
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                break
        else:
            sosu.append(num)
    if len(sosu) == 0:
        print(-1)
    else:
        print(sum(sosu), sosu[0], sep="\n")


if __name__ == '__main__':
    M = int(input().strip())
    N = int(input().strip())
    solution(M, N)