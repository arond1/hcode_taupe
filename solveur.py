def solveur(slice, types, values):
    res = []
    total = 0
    for i in range(0, len(values)):
        if(total + values[i] <= slice):
            res.append(i)
            total += values[i]
    return [total, res]
