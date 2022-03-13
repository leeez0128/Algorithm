import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline


def NQueen(count, N):
    global result
    if count == N:
        result += 1
        return

    for i in range(N):
        queen[count] = i
        for j in range(count):
            if queen[j] == queen[count] or abs(queen[j] - queen[count]) == (count - j):
                break
        else:
            NQueen(count+1, N)


if __name__ == '__main__':
    N = int(input().strip())
    queen = [0]*N
    result = 0
    NQueen(0, N)
    print(result)
