
def read_file() -> tuple:
    left: list = []
    right:list = []
    with open('input.txt', 'r') as file:
        for line in file:
            left.append(int(line.strip().split()[0]))
            right.append(int(line.strip().split()[1]))
    return left, right

def solution_1() -> int:
    res: int = 0
    left, right = read_file()
    for _ in range(len(left)):
        res += abs(min(left)-min(right))
        left.remove(min(left))
        right.remove(min(right))
    return res

def solution_2() -> int:
    res: int = 0
    left, right = read_file()
    for i in left:
        res += i * right.count(i)
    return res

print(solution_1())
print(solution_2())
