import sys
input = sys.stdin.readline


def solution(A, B, C):
    if B == 1:
        return A % C
    
    result = solution(A, B // 2, C)
    
    if B % 2 == 0:
        return result**2 % C
    else:
        return result**2*A % C


if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    print(solution(A, B, C))
