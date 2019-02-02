def merge(left, right):
    sorted_list = []

    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    if left:
        sorted_list.extend(left)
    else:
        sorted_list.extend(right)

    return sorted_list


def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        return merge(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))


print(merge_sort([3,6,2,1,6,7,8,11,3]))
