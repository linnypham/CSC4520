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
    for i in range(len(shorter)):
        for j in range(len(longer)):
            if shorter[i] == longer[j]:
                output.append(shorter[i])
                longer[j] = 0

    return output


