import sys
input = sys.stdin.readline


def solution(word):
    freq = dict()

    for i in range(len(word)):
        if word[i] in freq:
            freq[word[i]] += 1
        else:
            freq[word[i]] = 1

    sortFreq = sorted(freq.items(), key= lambda val:val[1], reverse=True)
    maxi = 0
    result = ''
    flag = 0
    for key, value in sortFreq:
        if maxi == value:
            print("?")
            return
        if maxi != value:
            if flag != 0:
                break
            else:
                maxi = value
                result = key
                flag = 1
        
    print(result.upper())


if __name__ == '__main__':
    word = input().strip().lower()
    solution(word)
