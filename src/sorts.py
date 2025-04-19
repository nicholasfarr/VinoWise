def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
       
        if left[i][1] >= right[j][1]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged



def quick_sort(items, low=0, high=None):
    if high is None:
        high = len(items) - 1
    def partition(lo, hi):
        pivot = items[hi][1]
        i = lo - 1
        for j in range(lo, hi):
            if items[j][1] >= pivot:  
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i+1], items[hi] = items[hi], items[i+1]
        return i+1

    while low < high:
        p = partition(low, high)

        #used tail call optimization referenced this article. https://www.geeksforgeeks.org/quicksort-tail-call-optimization-reducing-worst-case-space-log-n/
        if p - low < high - p:
            quick_sort(items, low, p - 1)
            low = p + 1
        else:
            quick_sort(items, p + 1, high)
            high = p - 1
    return items