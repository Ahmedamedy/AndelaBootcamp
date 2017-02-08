def find_max_min(n):

    n.sort()

    if n[0] == n[-1]:
        return [len(n)]
        
    else:
        max_n = n[0]
        min_n = n[-1]

        return [max_n,min_n]
