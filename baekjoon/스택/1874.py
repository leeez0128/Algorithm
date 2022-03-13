import sys
input = sys.stdin.readline


def solution(n, seq):
    stack = []
    answer = []
    temp = 0
    
    for num in seq:
        for i in range(temp+1, num+1):
            stack.append(i)
            answer.append("+")
        if num == stack[-1]:
            stack.pop()
            temp = max(temp, num)
            answer.append("-")
    
    if stack:
        print("NO")
        return
        
    print("\n".join(answer))
                

if __name__ == '__main__':
    n = int(input().strip())
    seq = []
    for _ in range(n):
        seq.append(int(input().strip()))
    solution(n, seq)
