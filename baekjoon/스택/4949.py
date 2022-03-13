import sys
input = sys.stdin.readline


def solution(sen):
    stack = []
        
    for ch in sen:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(0)
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(0)
                break
    
    if stack:
        print("no")
    else:
        print("yes")


if __name__ == '__main__':
    while True:
        sen = input().rstrip()
        if sen == '.':
            break
        solution(sen)
