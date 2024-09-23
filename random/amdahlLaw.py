def amdahl(S,N):
    return 1/(S+(1-S)/N)
print(amdahl(0.60,4))
