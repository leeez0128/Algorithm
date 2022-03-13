import sys
input = sys.stdin.readline


def solution(seq):
    cnt = 0
    for quiz in seq:
        score = 0
        for i in range(len(quiz)):
            if quiz[i] == 'O':
                cnt += 1
            else:
                cnt = 0
            score += cnt 
        cnt = 0
        print(score)


if __name__ == '__main__':
    T = int(input().strip())
    seq = [input().strip() for _ in range(T)]
    solution(seq)
