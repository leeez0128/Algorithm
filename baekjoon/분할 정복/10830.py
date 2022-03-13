import sys
input = sys.stdin.readline


def multiMatrix(N, matrix1, matrix2):
    result = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += matrix1[i][k] * matrix2[k][j] % 1000
            result[i].append(tmp)
    return result


def solution(N, B, seq):
    if B == 1:
        return seq
    result = solution(N, B//2, seq)
    multiResult = multiMatrix(N, result, result)

    if B % 2 == 0:
        return multiResult
    else:
        return multiMatrix(N, multiResult, seq)


def printResult(N, B, seq):
    square = solution(N, B, seq)
    for row in square:
        for col in row:
            print(col % 1000, end=" ")
        print()


if __name__ == '__main__':
    N, B = map(int, input().strip().split())
    seq = [list(map(int, input().strip().split())) for _ in range(N)]
    printResult(N, B, seq)
