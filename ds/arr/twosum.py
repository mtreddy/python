from collections import defaultdict
def two_sum(arr, target):
    tab = defaultdict(int)
    for ind in range(0, len(arr)):
        tmp = target - arr[ind]
        print(ind, arr[ind], tmp)
        if arr[ind] not in tab.keys():
            tab[tmp]=ind
        else:
            print(ind, tab[arr[ind]])
            print(tab)
            return True
    print(tab)
    return False

arr = [2,7,11,15]
two_sum(arr, 9)
