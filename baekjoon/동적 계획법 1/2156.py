import sys
input = sys.stdin.readline


def solution(podo):
    if len(podo) < 3:
        print(sum(podo))
        return

    dp = [0, podo[0], podo[0] + podo[1]]

    for i in range(3, len(podo)+1):
        dp.append(max(dp[i-1], podo[i-1] + podo[i-2] + dp[i-3], podo[i-1] + dp[i-2]))
    
    print(dp[-1])
    

if __name__ == '__main__':
    n = int(input().strip())
    podo = [int(input().strip()) for _ in range(n)]
    solution(podo)
