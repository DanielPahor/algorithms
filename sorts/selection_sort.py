import unittest

#O(n^2)
def selection_sort(items):
    for i in range(0, len(items)-1):
        index_of_smallest = i
        for j in range(i+1, len(items)):
            if items[j] < items[index_of_smallest]:
                index_of_smallest = j
        items[i], items[index_of_smallest] = items[index_of_smallest], items[i]

    return items

class Test(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(selection_sort([4, 3, 1]), [1, 3, 4])
        self.assertEqual(selection_sort([4, 5, 3, 1, 1]), [1, 1, 3, 4, 5])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([1, 1, 1, 4, 200, 4, 5, 6, 0, -1, -10, -5]), [-10, -5, -1, 0, 1, 1, 1, 4, 4, 5, 6, 200])


if __name__ == "__main__":
    unittest.main()
