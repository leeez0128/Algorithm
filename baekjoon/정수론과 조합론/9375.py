import sys
input = sys.stdin.readline


def solution(closet):
    result = 1
    for key in closet.keys():
        result *= (closet[key] + 1)
    
    print(result - 1)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        closet = dict()
        for _ in range(n):
            name, kind = input().strip().split()
            if kind in closet:
                closet[kind] += 1
            else:
                closet[kind] = 1
        solution(closet)
        