import sys
input = sys.stdin.readline


left_white = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

left_black = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]


def solution(N, M, board):
    paint = sys.maxsize
    for i in range(N-8+1):
        for j in range(M-8+1):
            black = 0
            white = 0
            for k in range(0,8):
                for l in range(0,8):
                    if board[i+k][j+l] != left_black[k][l]:
                        black += 1
                    if board[i+k][j+l] != left_white[k][l]:
                        white += 1
            paint = min(black, white, paint)
    
    print(paint)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    board = []
    for _ in range(N):
        board.append((input().strip()))
    solution(N, M, board)
