def reverse(lst):
    for i in range(len(lst)):
        j = len(lst) - i
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
