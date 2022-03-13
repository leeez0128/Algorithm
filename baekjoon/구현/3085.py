import sys
input = sys.stdin.readline

long_candy = 0


def game(N, candy):
    global long_candy
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
                long_candy = max(long_candy, cnt)
            else:
                cnt = 1


def solution(N, candy):
    for i in range(N):
        for j in range(N-1):
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
            game(N, candy)
            trans_candy = [list(x) for x in zip(*candy)]
            game(N, trans_candy)
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]

    for i in range(N):
        for j in range(N-1):
            candy[j][i],candy[j+1][i] = candy[j+1][i],candy[j][i]
            game(N, candy)
            trans_candy = [list(x) for x in zip(*candy)]
            game(N, trans_candy)
            candy[j][i],candy[j+1][i] = candy[j+1][i],candy[j][i]
  
    print(long_candy)


if __name__ == '__main__':
    N = int(input().strip())
    candy = []
    for _ in range(N):
        candy.append(list(input().strip()))
    solution(N, candy)
