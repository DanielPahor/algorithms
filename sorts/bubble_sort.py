import unittest

#O(n^2)
def bubble_sort(items):
    for i in range(len(items)-1, 0, -1):
        for j in range(0, i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items

class Test(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(bubble_sort([4, 3, 1]), [1, 3, 4])
        self.assertEqual(bubble_sort([4, 5, 3, 1, 1]), [1, 1, 3, 4, 5])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([1, 1, 1, 4, 200, 4, 5, 6, 0, -1, -10, -5]), [-10, -5, -1, 0, 1, 1, 1, 4, 4, 5, 6, 200])

if __name__ == "__main__":
    unittest.main()
