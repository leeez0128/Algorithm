import sys
input = sys.stdin.readline


def solution(E, S, M):
    e, s, m = 0, 0, 0
    year = 0

    while True:
        if e == E and s == S and m == M:
            print(year)
            return
        e += 1
        s += 1
        m += 1
        year += 1

        if e == 16: e = 1
        if s == 29: s = 1
        if m == 20: m = 1
            

if __name__ == '__main__':
    E, S, M = map(int, input().strip().split())
    solution(E, S, M)
