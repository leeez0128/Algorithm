import sys
input = sys.stdin.readline


def operation(st, state, num):
    if state == 'push':
        st.append(num)
    elif state == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif state == 'size':
        print(len(st))
    elif state == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif state == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
    return st
        

def solution(N, orders):
    st = []
    for order in orders:
        num = 0
        if len(order.split(" ")) != 1:
            num = order.split(" ")[1]
        state = order.split(" ")[0]
        st = operation(st, state, num)


if __name__ == '__main__':
    N = int(input().strip())
    orders = []
    for _ in range(N):
        orders.append(input().strip())
    solution(N, orders)
        