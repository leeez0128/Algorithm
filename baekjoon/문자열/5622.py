import sys
input = sys.stdin.readline


def solution(dial):
    result = 0
    for elem in dial:
        elem_a = int(ord(elem)) - 65
        if elem_a <= 2:
            result += 3
        elif 2 < elem_a and elem_a <= 5:
            result += 4
        elif 5 < elem_a and elem_a <= 8:
            result += 5
        elif 8 < elem_a and elem_a <= 11:
            result += 6
        elif 11 < elem_a and elem_a <= 14:
            result += 7
        elif 14 < elem_a and elem_a <= 18:
            result += 8
        elif 18 < elem_a and elem_a <= 21:
            result += 9
        elif 21 < elem_a and elem_a <= 25:
            result += 10
    print(result)


if __name__ == '__main__':
    dial = input().strip()
    solution(dial)
