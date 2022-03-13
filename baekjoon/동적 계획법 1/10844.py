import sys
input = sys.stdin.readline


def solution(N):
    stairNumber = [[0]*10 for _ in range(N)]
    stairNumber[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    MOD = 10**9
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                stairNumber[i][j] = stairNumber[i-1][j+1]
            elif j == 9:
                stairNumber[i][j] = stairNumber[i-1][j-1]
            else:
                stairNumber[i][j] = stairNumber[i-1][j-1] + stairNumber[i-1][j+1]
    
    print(sum(stairNumber[N-1]) % MOD)
        

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
