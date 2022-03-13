import sys
input = sys.stdin.readline


def solution(N, M, square):
    res = 0
    
    for i in range(N-1):
        for j in range(M-1):
            dist = min(N-i, M-j) - 1
            edge = square[i][j]

            while dist >= res:
                if square[i][j+dist] == edge and square[i+dist][j] == edge and square[i+dist][j+dist] == edge:
                    res = dist + 1
                dist -= 1
    if res == 0:
        print(1)
        return

    print((res)**2)
                        

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    square = [input().strip() for _ in range(N)]
    solution(N, M, square)
