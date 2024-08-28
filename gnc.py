from factor import factor
def gnc(m,n):
    a = factor(m)
    b = factor(n)
    output = []
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    for i in shorter:
        if i in shorter and i in longer:
            output.append(i)

    return output

print(gnc(12,18))
