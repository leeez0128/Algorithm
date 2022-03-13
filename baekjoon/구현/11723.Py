import sys
input = sys.stdin.readline

S = set()

def operation(operator):
    global S

    if(len(operator) == 1):
        if operator[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        op, element = operator[0], int(operator[1])
        if op == 'add':
            S.add(element)
        elif op == 'remove':
            S.discard(element)
        elif op == 'check':
            if element in S:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if element in S:
                S.discard(element)
            else:
                S.add(element)


if __name__ == '__main__':
    M = int(input().strip())
    for _ in range(M):
        operator = input().strip().split()
        operation(operator)
