import sys
from collections import deque
input = sys.stdin.readline


def solution(p, n, arr):
    rev = 0
    
    for i in range(len(p)):
        if p[i] == 'R':
            rev += 1
        else: # 'D'
            if len(arr) == 0 or arr[0] == '':
                print("error")
                return
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if rev % 2 == 0:
        print("[", ",".join(arr), "]", sep="")
    else:
        arr.reverse()
        print("[", ",".join(arr), "]", sep="")
    

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        p = input().strip()
        n = int(input().strip())
        arr = deque(input().strip()[1:-1].split(","))
        solution(p, n, arr)