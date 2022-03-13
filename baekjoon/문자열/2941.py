import sys
input = sys.stdin.readline

# 이렇게 풀린다는게 좀 이상..한데?...
# def solution(word):
#     cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#     result = 0
#     for atia in cro:
#         result += word.count(atia)
    
#     print(len(word)-result)

# 모범답안
def solution(word):
    cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for atia in cro:
        word = word.replace(atia, "*")
    print(len(word))


if __name__ == '__main__':
    word = input().strip()
    solution(word)