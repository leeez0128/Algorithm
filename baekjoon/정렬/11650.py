import sys
input = sys.stdin.readline


def solution(coordinate):
    sorted_coordinate = sorted(coordinate, key=lambda x:(x[0], x[1]))
    for i in range(len(coordinate)):
        print(sorted_coordinate[i][0], sorted_coordinate[i][1], sep=" ")


if __name__ == '__main__':
    N = int(input().strip())
    coordinate = []
    for _ in range(N):
        coordinate.append(list(map(int, input().strip().split())))
    solution(coordinate)
