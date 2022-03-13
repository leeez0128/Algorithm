import sys
input = sys.stdin.readline


def check_dia(result):
    dia, ok = 0, 0
    for i in range(5):
        if result[4-i][i] == 1:
            ok += 1
    if ok == 5:
        dia += 1
    ok = 0

    for i in range(5):
        if result[i][i] == 1:
            ok += 1
    if ok == 5:
        dia += 1

    return dia


def check_col(result):
    col = 0
    for i in range(5):
        if list(map(list, zip(*result)))[i] == [1,1,1,1,1]:
            col += 1
    return col


def check_row(result):
    row = 0
    for i in range(5):
        if result[i] == [1,1,1,1,1]:
            row += 1
    return row


def solution(bingo, answer):
    result = [[0]*5 for _ in range(5)] #철수 빙고판 채점판
    for i in range(5):
        for j in range(5):
            key = bingo[answer[i][j]] #철수 빙고판에서 사회자가 부른 수의 위치 
            result[key//5][key%5] = 1
            res = check_row(result) + check_col(result) + check_dia(result)
            if res >= 3:
                return 5*i + (j+1)


if __name__ == '__main__':
    bingo = dict()
    answer = []
    cnt = 0
    for i in range(10):
        if i > 4:
            answer.append(list(map(int, input().strip().split())))
        else:
            numbers = list(map(int, input().strip().split()))
            for j in range(5):
                bingo[numbers[j]] = cnt
                cnt += 1
    print(solution(bingo, answer))
