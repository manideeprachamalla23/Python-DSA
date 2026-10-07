def linearSearch(a,e):
    for i in range(len(a)):
        if a[i] == e:
            return i
    return -1



a=[1,11,12,9,18,2]
print(linearSearch(a,22))




def linearSearch(a,e):
    for i in range(len(a)):
        if a[i] == e:
            print(f"Element {e} is found at index {i}")
            return i
    return -1



a=[1,11,12,9,18,2]
print(linearSearch(a,12))