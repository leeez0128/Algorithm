import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def multiple(_sum, cnt):
    if len(_sum) == 1:
        print(cnt)
        _sum = int(_sum)
        if _sum == 3 or _sum == 6 or _sum == 9:
            print("YES")
        else:
            print("NO")
        return

    new_sum = 0
    for num in _sum:
        new_sum += int(num)
    
    return multiple(str(new_sum), cnt+1)


if __name__ == '__main__':
    X = input().strip()
    cnt = 0
    multiple(X, cnt)   
