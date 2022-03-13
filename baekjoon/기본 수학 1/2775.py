import sys
input = sys.stdin.readline


def solution(kn):
    k = kn[0]
    n = kn[1]
    residents = [i for i in range(1, n+1)]
    if n == 1:
        print(1)
        return
    for _ in range(k):
        for i in range(1, n):
            residents[i] += residents[i-1]
    
    print(residents[-1])


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        kn = [int(input().strip()) for _ in range(2)]
        solution(kn)
