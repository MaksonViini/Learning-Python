def bubble_sort(item):
    n = len(item)
    for i in range(n):
        for j in range(n-i-1):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]
                print(item)
    return item


print(bubble_sort([5, 1, 4, 2]))
