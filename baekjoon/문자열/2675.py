import sys
input = sys.stdin.readline


def solution(repeat, seq):
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            print(seq[i][j]*repeat[i], end="")
        print()


if __name__ == '__main__':
    T = int(input().strip())
    repeat = []
    seq = []
    for _ in range(T):
        R, S = input().strip().split()
        repeat.append(int(R))
        seq.append(S)
    solution(repeat, seq)
