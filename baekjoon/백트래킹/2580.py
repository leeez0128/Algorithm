import sys
input = sys.stdin.readline


def dfs(depth):
    if depth == blank:
        for num in sdoqu:
            print(' '.join(map(str, num)))
        sys.exit(0)
    
    y, x = possible[depth]
    for n in range(1, 10):
        if not row[y][n] and not col[x][n] and not box[y//3 * 3 + x//3][n]:
            row[y][n] = col[x][n] = box[y//3 * 3 + x//3][n] = True
            sdoqu[y][x] = n
            dfs(depth+1)
            row[y][n] = col[x][n] = box[y//3 * 3 + x//3][n] = False
            sdoqu[y][x] = 0


if __name__ == '__main__':
    sdoqu = [list(map(int, input().strip().split())) for _ in range(9)]
    row = [[False]*10 for _ in range(10)]
    col = [[False]*10 for _ in range(10)]
    box = [[False]*10 for _ in range(10)]

    possible = []
    for r in range(9):
        for c in range(9):
            if not sdoqu[r][c]:
                possible.append([r, c])
            else:
                row[r][sdoqu[r][c]] = True
                col[c][sdoqu[r][c]] = True
                box[r//3 * 3 + c//3][sdoqu[r][c]] = True
    
    blank = len(possible)
    dfs(0)
