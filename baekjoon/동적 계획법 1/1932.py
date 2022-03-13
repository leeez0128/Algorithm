import sys
input = sys.stdin.readline


def solution(triangle):  
    if len(triangle) == 1:
        print(triangle[0][0])
        return
    
    for height in range(1, len(triangle)):
        if height == 1:
            triangle[height][0] += triangle[0][0]
            triangle[height][1] += triangle[0][0]
        else:
            for i in range(height+1):
                if i == 0:
                    triangle[height][i] += triangle[height-1][0]
                elif i == height:
                    triangle[height][i] += triangle[height-1][i-1]
                else:
                    triangle[height][i] += max(triangle[height-1][i-1], triangle[height-1][i])
    
    print(max(triangle[height]))


if __name__ == '__main__':
    n = int(input().strip())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().strip().split())))
    solution(triangle)
