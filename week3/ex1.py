def sop(*args, op='+'):
    result = 0
    if op == '*':
        result = 1
        for a in args:
            result *= a
        return result
    elif op == '+':
        for a in args:
            result += a
        return result
    else:
        return 'error'


print(sop(1, 2, 3, 4, 5, op='*'));
