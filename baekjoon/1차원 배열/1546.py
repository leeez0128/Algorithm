import sys
input = sys.stdin.readline


def solution(N, score):
    sumOfScores = 0
    for i in range(N):
        sumOfScores += score[i]/max(score) * 100

    print(sumOfScores / N)


if __name__ == '__main__':
    N = int(input().strip())
    score = list(map(int, input().strip().split()))
    solution(N, score)
