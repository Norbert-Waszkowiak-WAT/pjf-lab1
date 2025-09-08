import unittest
from solution import Solution


class TestZad1_Smoke(unittest.TestCase):
    def test_0(self):
        s = "XIV"
        expected = 14
        result = Solution.romanToInt(s)
        assert result == expected


class TestZad2_Smoke(unittest.TestCase):
    def test_0(self):
        n = 5
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        result = Solution.fizzbuzz(n)
        assert result == expected


class TestZad3_Smoke(unittest.TestCase):
    def test_0(self):
        weight = 70
        height = 1.75
        expected = 22.86
        result = Solution.bmi(weight, height)
        assert result == expected


class TestZad4_Smoke(unittest.TestCase):
    def test_0(self):
        n = 13
        expected = True
        result = Solution.prime_number(n)
        assert result == expected


class TestZad5_Smoke(unittest.TestCase):
    def test_0(self):
        s = "hello"
        letter = "l"
        expected = 2
        result = Solution.count_letter_in_string(s, letter)
        assert result == expected


class TestZad6_Smoke(unittest.TestCase):
    def test_0(self):
        n = 10
        expected = 25
        result = Solution.sum_of_odd_numbers(n)
        assert result == expected


class TestZad7_Smoke(unittest.TestCase):
    def test_0(self):
        l1 = [1, 2, 3, 4]
        l2 = [2, 3, 5]
        expected = [2, 3]
        result = Solution.inner_join_two_sorted_lists(l1, l2)
        assert result == expected


class TestZad8_Smoke(unittest.TestCase):
    def test_0(self):
        haystack = "hello"
        needle = "o"
        expected = 4
        result = Solution.find_index_of_first_occurrence_of_element_in_string(haystack, needle)
        assert result == expected


class TestZad9_Smoke(unittest.TestCase):
    def test_0(self):
        l1 = [1, 2, 3, 4]
        l2 = [2, 3, 4, 5]
        expected = [1, 5]
        result = Solution.outer_join_two_sorted_lists(l1, l2)
        assert result == expected


class TestZad0_Smoke(unittest.TestCase):
    def test_0(self):
        a = Solution.ListNode(1)
        b = Solution.ListNode(2, a)
        a.next = b  # cykl: 1 -> 2 -> 1
        expected = True
        result = Solution.linked_list_cycle(a)
        assert result == expected


if __name__ == "__main__":
    unittest.main()
