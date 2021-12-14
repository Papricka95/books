def operations(a, b, c):
    result = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
    }[c]
    return result
