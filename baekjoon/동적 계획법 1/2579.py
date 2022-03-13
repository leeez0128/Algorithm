import sys
input = sys.stdin.readline


def climbingStairs(stairs):
    dp = []
    if len(stairs) <= 2:
        print(sum(stairs))
        return
    
    dp.append(stairs[0])
    dp.append(max(stairs[0] + stairs[1], stairs[1]))
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

    for i in range(3, len(stairs)):
        dp.append(max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]))

    print(dp[-1])


if __name__ == '__main__':
    num = int(input().strip())
    stairs = [int(input().strip()) for _ in range(num)]
    climbingStairs(stairs)
