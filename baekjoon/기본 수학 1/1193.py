import sys
input = sys.stdin.readline


def solution(X):
    line = 1
    while line < X:
        X -= line
        line += 1
    
    if line % 2 == 1:
        up = line - X + 1
        low = X
    else:
        up = X
        low = line - X + 1 
    
    print(up, '/', low, sep="")


if __name__ == '__main__':
    X = int(input().strip())
    solution(X)
