import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def star(N):
    if N == 1:
        return ['*']
    N //= 3
    _shape = star(N)
    top_and_bottom = [i*3 for i in _shape]
    middle = [i + (' ' * N) + i for i in _shape]
    return top_and_bottom + middle + top_and_bottom


if __name__ == '__main__':
    N = int(input().strip())
    shape = '\n'.join(star(N))
    print(shape)
