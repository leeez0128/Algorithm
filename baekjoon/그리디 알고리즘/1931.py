import sys
input = sys.stdin.readline


def solution(N, meetings):
    count = 1
    meetings = sorted(meetings, key=lambda x: x[0])
    meetings = sorted(meetings, key=lambda x: x[1])

    end = meetings[0][1] # first meeting end time
    for i in range(1, N):
        if meetings[i][0] >= end:
            count += 1
            end = meetings[i][1]
    
    print(count)


if __name__ == '__main__':
    N = int(input().strip())
    meetings = []
    for _ in range(N):
        meetings.append(list(map(int, input().strip().split())))
    solution(N, meetings)
