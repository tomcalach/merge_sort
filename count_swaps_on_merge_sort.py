def countInversions(arr):
    class Counter:
        def __init__(self, counter=0):
            self.counter = counter

        def merge_with_count(self, left, right):
            sorted_list = []
            left_len = len(left)
            right_len = len(right)
            left_ind = 0
            right_ind = 0
            while left_len > left_ind and right_len > right_ind:
                if left[left_ind] <= right[right_ind]:
                    sorted_list.append(left[left_ind])
                    left_ind += 1
                else:
                    self.counter += left_len - left_ind
                    sorted_list.append(right[right_ind])
                    right_ind += 1

            if left_len == left_ind:
                sorted_list.extend(right[right_ind:])
            else:
                sorted_list.extend(left[left_ind:])
            return sorted_list

        def merge_sort(self, l):
            length = len(l)
            mid = length//2
            if length < 2:
                return l
            else:
                return self.merge_with_count(self.merge_sort(l[:mid]), self.merge_sort(l[mid:]))

    count_inversions = Counter()
    count_inversions.merge_sort(arr)
    return count_inversions.counter


print(countInversions([1,2,3,2,1]))
print(countInversions([1,1,1,2,2]))