import sys
input = sys.stdin.readline


def cnt(color):
    global minus, zero, one
    if color == -1:
        minus += 1
        return
    elif color == 0:
        zero += 1
        return
    else:
        one += 1
        return


def cut(x, y, N, square):
    color = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != square[i][j]:
                cut(x, y, N//3, square)
                cut(x+N//3, y, N//3, square)
                cut(x+2*N//3, y, N//3, square)
                cut(x, y+N//3, N//3, square)
                cut(x, y+2*N//3, N//3, square)
                cut(x+N//3, y+N//3, N//3, square)
                cut(x+2*N//3, y+N//3, N//3, square)
                cut(x+N//3, y+2*N//3, N//3, square)
                cut(x+2*N//3, y+2*N//3, N//3, square)
                return
    
    cnt(color)


def solution(N, square):
    global minus, zero, one
    cut(0, 0, N, square)
    print(minus, zero, one, sep="\n")


if __name__ == '__main__':
    N = int(input().strip())
    square = []
    minus, zero, one = 0, 0, 0
    for _ in range(N):
        square.append(list(map(int, input().strip().split())))
    solution(N, square)
