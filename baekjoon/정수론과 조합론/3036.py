from os import sep
import sys, math
input = sys.stdin.readline


def gcd_(rings, src):
    first = rings[0]
    gcd = 1
    for i in range(2, src+1):
        while (first % i == 0) and (src % i == 0):
            first = math.floor(first // i)
            src = math.floor(src // i)
            gcd *= i
            continue
    return gcd


def solution(N, rings):
    for i in range(1, N):
        gcd = gcd_(rings, rings[i])
        print(rings[0] // gcd, "/", rings[i] // gcd, sep="")
    

if __name__ == '__main__':
    N = int(input().strip())
    rings = list(map(int, input().strip().split()))
    solution(N, rings)
