import sys
input = sys.stdin.readline


def solution(N):
    mok = N // 3
    turn = N - mok * 3 + mok
    
    if turn % 2 == 0:
        print("CY")
    else:
        print("SK")
        

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
