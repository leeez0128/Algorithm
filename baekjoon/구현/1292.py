import sys
input = sys.stdin.readline

seq = [0]

def solution(A, B):
    for i in range(B+1):
        for _ in range(i):
            seq.append(i)
            if len(seq) >= (B+1):
                return


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    solution(A, B)
    print(sum(seq[A:B+1]))
