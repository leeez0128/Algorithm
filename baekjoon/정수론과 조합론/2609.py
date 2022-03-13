import sys, math
input = sys.stdin.readline


def solution(A, B):
    gcd = 1
    for i in range(2, min(A, B)+1):
        while((A % i == 0) and (B % i == 0)):
            A = math.floor(A // i)
            B = math.floor(B // i)
            gcd *= i
            continue

    lcm = A * B * gcd
    print(gcd, lcm, sep="\n")


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    solution(A, B)
