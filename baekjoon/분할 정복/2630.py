import sys
input = sys.stdin.readline


def cnt(color):
    global white, blue
    # 0 : white / 1: blue
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return   


def cut(x, y, N, square):
    color = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != square[i][j]:
                cut(x, y, N//2, square)
                cut(x+N//2, y, N//2, square)
                cut(x, y+N//2, N//2, square)
                cut(x+N//2, y+N//2, N//2, square)
                return
    
    cnt(color)
    

def solution(N, square):
    global white, blue
    cut(0, 0, N, square)
    print(white, blue, sep="\n")
    

if __name__ == '__main__':
    N = int(input().strip())
    square = []
    white, blue = 0, 0
    for _ in range(N):
        square.append(list(map(int, input().strip().split())))
    solution(N, square)
        