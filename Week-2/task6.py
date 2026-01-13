def all(lst):
    max_len = max(len(s) for s in lst)
    result = []
    for s in lst:
        if len(s) < max_len:
            s = s + "_" * (max_len - len(s))
        result.append(s)

    return result
data = ["Aset", "Madi", "Nurkhan"]
print(all(data))
