import sys
input = sys.stdin.readline


def solution(PS):
    ps = []
    for i in range(len(PS)):
        if PS[i] == '(':
            ps.append('(')
        else:
            if '(' in ps:
                ps.pop()
            else:
                print("NO")
                return
            
    if len(ps) == 0:
        print("YES")
        return
    else:
        print("NO")
        return


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        solution(input().strip())
