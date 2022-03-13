import sys
input = sys.stdin.readline


def solution(seq):
    answer = []
    for i in range(len(seq)):
        answer.append(seq[i]%42)
    answerSet = set(answer)
    print(len(answerSet))


if __name__ == '__main__':
    seq = [int(input().strip()) for _ in range(10)]
    solution(seq)
