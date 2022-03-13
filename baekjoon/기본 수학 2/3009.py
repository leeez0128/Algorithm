import sys
input = sys.stdin.readline


def solution(squareX, squareY):
    for i in range(3):
        if squareX.count(squareX[i]) == 1:
            resultX = squareX[i]
        if squareY.count(squareY[i]) == 1:
            resultY = squareY[i]
    
    print(resultX, resultY)


if __name__ == '__main__':
    squareX = []
    squareY = []
    for _ in range(3):
        x, y = map(int, input().strip().split())
        squareX.append(x)
        squareY.append(y)
    solution(squareX, squareY)
