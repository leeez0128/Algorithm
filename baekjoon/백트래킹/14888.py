import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
mini = 1e9
maxi = -1e9


def BackTracking(count, result, A, plus, minus, multi, div):
    global mini, maxi
    if count == len(A):
        mini = min(result, mini)
        maxi = max(result, maxi)
        return

    if plus:
        BackTracking(count+1, result + A[count], A, plus - 1, minus, multi, div)
    if minus:
        BackTracking(count+1, result - A[count], A, plus, minus - 1, multi, div)
    if multi:
        BackTracking(count+1, result * A[count], A, plus, minus, multi - 1, div)
    if div:
        BackTracking(count+1, int(result / A[count]), A, plus, minus, multi, div - 1)


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    operator = list(map(int, input().strip().split()))
    BackTracking(1, A[0], A, operator[0], operator[1], operator[2], operator[3])
    print(maxi, mini, sep = "\n")