import sys
input = sys.stdin.readline


def solution(A, B, C):
    A += C // 60
    B += C % 60
    
    if B >= 60:
        A += 1
        B -= 60
    if A >= 24:
        A -= 24
    
    print(A, B)


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    C = int(input().strip())
    solution(A, B, C)
