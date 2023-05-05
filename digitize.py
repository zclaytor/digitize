from numpy.random import choice


operations = ["+", "-", "*", "/"]


def solve(n, target):
    s = 0
    while s != target:
        nn = choice(n, size=len(n), replace=False)
        ops = choice(operations, size=len(n)-1)
        s = nn[0]
        op_str = f"{s}"
        for i in range(1, len(n)-1):
            op_str += f"{ops[i]}{nn[i]}"
            if ops[i] == "+":
                s += nn[i]
            elif ops[i] == "-":
                s -= nn[i]
            elif ops[i] == "*":
                s *= nn[i]
            elif s % nn[i] == 0:
                s /= nn[i]
            if s < 0 or isinstance(s, float): break
    return op_str+f"={int(s)}"

