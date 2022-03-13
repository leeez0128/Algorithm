import sys
input = sys.stdin.readline


def solution(formula):
    splited_formula = formula.split("-")
    
    for i in range(len(splited_formula)):
        plus_elem = splited_formula[i].split("+")
        splited_formula[i] = 0
        for num in plus_elem:
            splited_formula[i] += int(num)
    
    result = splited_formula[0]

    for i in range(1, len(splited_formula)):
        result -= splited_formula[i]
    
    print(result)


if __name__ == '__main__':
    formula = input().strip()
    solution(formula)
