def horspool(text,pattern):
    u_pattern = []
    shift = {}
    for char in pattern:
        if char not in u_pattern:
            u_pattern.append(char)
    
    n = len(pattern)
    for i in range(n-1,-1,-1):
        for char in u_pattern:
            if char == pattern[i]:
                