def setting(data):
    return data[1]


arr = [('banana', 2), ('apple', 5), ('carrot', 3)]
result = sorted(arr, key=setting)
print(result)