import sys
input = sys.stdin.readline

# 시간 초과
# def solution(N, A, M, B):
#     for b in B:
#         if b in A:
#             print(1)
#         else:
#             print(0)


def binary_search(element, A, start=0, end=None):
    if end == None:
        end = len(A) - 1
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if element == A[mid]:
        return 1
    elif element < A[mid]:
        end = mid - 1
    elif element > A[mid]:
        start = mid + 1
        
    return binary_search(element, A, start, end)


def solution(N, A, M, B):
    A = sorted(A)
    for b in B:
        print(binary_search(b, A))


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))
    solution(N, A, M, B)