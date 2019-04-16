import unittest

# O(nm) space and time
# O(n + m) space if cache previous row and col only
def sequence_alignment_cost(mismatch_cost, gap_cost, str1, str2):
    m = [[None for j in range(len(str1)+1)] for i in range(len(str2)+1)]

    # base cases
    for j in range(len(str1)+1):
        m[0][j] = gap_cost * j

    for i in range(len(str2)+1):
        m[i][0] = gap_cost * i

    # fill matrix
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            cost_of_matching = 0 if str1[j-1] == str2[i-1] else 1
            m[i][j] = min(cost_of_matching + m[i-1][j-1], gap_cost + m[i-1][j], gap_cost + m[i][j-1])

    return m[len(str2)][len(str1)]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence_alignment_cost(1, 1, 'abcdefghi', 'a'), 8)
        self.assertEqual(sequence_alignment_cost(1, 1, 'a', 'a'), 0)
        self.assertEqual(sequence_alignment_cost(5, 3, 'a', 'a'), 0)
        self.assertEqual(sequence_alignment_cost(5, 3, 'ab', 'a'), 3)
        self.assertEqual(sequence_alignment_cost(1, 1, 'abcdefghi', 'abcd'), 5)
        self.assertEqual(sequence_alignment_cost(1, 1, 'bcdefghi', 'abcd'), 6)

if __name__ == "__main__":
    unittest.main()
