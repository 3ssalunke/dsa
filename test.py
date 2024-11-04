def encode(strs):
    if not strs:
        return ""
    sizes, res = [], ""
    for s in strs:
        sizes.append(len(s))
    for sz in sizes:
        res += str(sz)
        res += ','
    res += '#'
    for s in strs:
        res += s
    print(res)
    return res