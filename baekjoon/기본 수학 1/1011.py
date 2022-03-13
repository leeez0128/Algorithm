import sys
input = sys.stdin.readline


def solution(x, y):
    distance = y - x
    max_distance = 1
    move_cnt = 1
    move_max = 1
    while not distance <= max_distance:
        max_distance += move_max
        move_cnt += 1
        if move_cnt % 2 == 0:
            move_max += 1

    print(move_cnt)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        x, y = map(int, input().strip().split())
        solution(x, y)
