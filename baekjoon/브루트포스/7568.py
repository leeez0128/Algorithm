import sys
input = sys.stdin.readline


def solution(people):
    ranking = [1]*len(people)
    for i in range(len(people)):
        k = 0
        for j in range(len(people)):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                k += 1
        ranking[i] = k+1

    for rank in ranking:
        print(rank, end=" ")       


if __name__ == '__main__':
    N = int(input().strip())
    people = []
    for _ in range(N):
        info = list(map(int, input().strip().split()))
        people.append(info)
    solution(people)
