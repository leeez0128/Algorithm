import sys
import math
input = sys.stdin.readline


# def solution(room):
#     # 1 - 1
#     # 2~7 - 7
#     # 8~19 - 19
#     # 20~37 - 37
#     # 계차수열 A(n+1) - A(N) = B(N)
#     # B(N) = 6N
#     # A(N) = sum(B(N)) + A(1)
#     #      = 3n(n-1) + 1
#     # room < 3n(n-1) + 1
#     # n >= (3+math.sqrt(9-12*(1-room))) // 6
#     if room == 1:
#         print(1)
#         return
#     num = int((3+math.sqrt(9-12*(1-room))) // 6)
#     result = 3*num*(num-1) + 1
#     if result == room:
#         print(num)
#         return
#     else:
#         print(num+1)
#         return


def solution(room):
    increase = 1
    how = 6
    numOfRoom = 1
    while room > increase:
        numOfRoom += 1
        increase += how
        how += 6
    print(numOfRoom)


if __name__ == '__main__':
    room = int(input().strip())
    solution(room)
