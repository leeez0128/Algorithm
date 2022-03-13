import sys
input = sys.stdin.readline


def cut(x, y, N, square):
    color = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != square[i][j]:
                print("(", end="")
                cut(x, y, N//2, square)
                cut(x, y+N//2, N//2, square)
                cut(x+N//2, y, N//2, square)
                cut(x+N//2, y+N//2, N//2, square)
                print(")", end="")
                return
    
    if color == 0:
        print('0', end="")
        return
    else:
        print('1', end="")
        return
    

def solution(N, square):
    cut(0, 0, N, square)
    

if __name__ == '__main__':
    N = int(input().strip())
    square = []
    for _ in range(N):
        square.append(list(map(int, input().strip())))
    solution(N, square)
        