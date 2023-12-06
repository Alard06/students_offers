def solve_equation(*args):
    if len(args) == 3:
        a, b, c = args
        if a == 0:
            if b == 0:
                if c == 0:
                    return ["*"]
                else:
                    return []
            else:
                x = -c / b
                return [x]
        else:
            D = b ** 2 - 4 * a * c
            if D < 0:
                return []
            elif D == 0:
                x = -b / (2 * a)
                return [x]
            else:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                return [x1, x2]
    elif len(args) == 2:
        b, c = args
        if b == 0:
            if c == 0:
                return ["*"]
            else:
                return []
        else:
            x = -c / b
            return [x]
    elif len(args) == 1:
        c = args[0]
        if c == 0:
            return ["*"]
        else:
            return []
    else:
        return None

print(solve_equation(-1, 7, 8))
print(solve_equation(2, 1, 1))
print(solve_equation(9, -6, 1))
print(solve_equation())
[-1.0, 8.0]
[]
[0.3333333333333333]
None

def test_solve_equation():
    assert solve_equation(-1, 7, 8) == [-1.0, 8.0]
    assert solve_equation(2, 1, 1) == []
    assert solve_equation(9, -6, 1) == [0.3333333333333333]
    assert solve_equation() == None
    print("OK")

test_solve_equation()

