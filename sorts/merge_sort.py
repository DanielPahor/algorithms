import unittest

#O(nlogn)
def merge_sort(items):
    if len(items) == 1:
        return items

    mid = len(items)//2
    left, right = items[:mid], items[mid:]

    left_merged, right_merged = merge_sort(left), merge_sort(right)

    return merge(left_merged, right_merged)

#O(n)
def merge(items_left, items_right):
    i = j = 0
    merged = []

    while i < len(items_left) and j < len(items_right):
        if items_left[i] < items_right[j]:
            merged.append(items_left[i])
            i += 1
        else:
            merged.append(items_right[j])
            j += 1

    if i < len(items_left):
        merged.extend(items_left[i:])

    if j < len(items_right):
        merged.extend(items_right[j:])

    return merged

class Test(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(merge_sort([4, 3, 1]), [1, 3, 4])
        self.assertEqual(merge_sort([4, 5, 3, 1, 1]), [1, 1, 3, 4, 5])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([1, 1, 1, 4, 200, 4, 5, 6, 0, -1, -10, -5]), [-10, -5, -1, 0, 1, 1, 1, 4, 4, 5, 6, 200])


if __name__ == "__main__":
    unittest.main()
