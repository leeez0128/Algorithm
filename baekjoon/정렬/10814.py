import sys
input = sys.stdin.readline


def solution(member):
    sorted_member = sorted(member, key=lambda x:(x[0], x[2]))
    for member in sorted_member:
        print(member[0], member[1], sep=" ")


if __name__ == '__main__':
    N = int(input().strip())
    member = []
    for i in range(N):
        age, name = input().strip().split()
        member.append([int(age), name, i])
    solution(member)
