import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def toja(H, Y):
    money = [0]*(Y+1)
    money[0] = H

    for year in range(1, Y+1):
        if (year - 1) >= 0 and money[year-1]:
            money[year] = max(int(money[year-1]*1.05), money[year])
        if (year - 3) >= 0 and money[year-3]:
            money[year] = max(int(money[year-3]*1.2), money[year])
        if (year - 5) >= 0 and money[year-5]:
            money[year] = max(int(money[year-5]*1.35), money[year])
    
    print(money[-1])


if __name__ == '__main__':
    H, Y = map(int, input().strip().split())
    toja(H, Y)
