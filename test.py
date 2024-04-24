import unittest

from solution import Solution


class TestZad1(unittest.TestCase):

    def test_0(self):
        s = "III"
        expected = 3
        result = Solution.romanToInt(s)
        assert result == expected

    def test_1(self):
        s = "IV"
        expected = 4
        result = Solution.romanToInt(s)
        assert result == expected

    def test_2(self):
        s = "LVIII"
        expected = 58
        result = Solution.romanToInt(s)
        assert result == expected

    def test_3(self):
        s = "MCMXCIV"
        expected = 1994
        result = Solution.romanToInt(s)
        assert result == expected


class TestZad2(unittest.TestCase):

    def test_0(self):
        n = 15
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                    "FizzBuzz"]
        result = Solution.fizzbuzz(n)
        assert result == expected

    def test_1(self):
        n = 1
        expected = ["1"]
        result = Solution.fizzbuzz(n)
        assert result == expected

    def test_2(self):
        n = 3
        expected = ["1", "2", "Fizz"]
        result = Solution.fizzbuzz(n)
        assert result == expected

    def test_3(self):
        n = 5
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        result = Solution.fizzbuzz(n)
        assert result == expected


class TestZad3(unittest.TestCase):

    def test_0(self):
        weight = 70
        height = 1.75
        expected = 22.86
        result = Solution.bmi(weight, height)
        assert result == expected

    def test_1(self):
        weight = 80
        height = 1.75
        expected = 26.12
        result = Solution.bmi(weight, height)
        assert result == expected

    def test_2(self):
        weight = 90
        height = 1.75
        expected = 29.39
        result = Solution.bmi(weight, height)
        assert result == expected

    def test_3(self):
        weight = 100
        height = 1.75
        expected = 32.65
        result = Solution.bmi(weight, height)
        assert result == expected


class TestZad4(unittest.TestCase):

    def test_0(self):
        n = 7
        expected = True
        result = Solution.prime_number(n)
        assert result == expected

    def test_1(self):
        n = 1
        expected = False
        result = Solution.prime_number(n)
        assert result == expected

    def test_2(self):
        n = 2
        expected = True
        result = Solution.prime_number(n)
        assert result == expected

    def test_3(self):
        n = 4
        expected = False
        result = Solution.prime_number(n)
        assert result == expected


class TestZad5(unittest.TestCase):

    def test_0(self):
        s = "hello"
        letter = "l"
        expected = 2
        result = Solution.count_letter_in_string(s, letter)
        assert result == expected

    def test_1(self):
        s = "hello"
        letter = "h"
        expected = 1
        result = Solution.count_letter_in_string(s, letter)
        assert result == expected

    def test_2(self):
        s = "hello"
        letter = "e"
        expected = 1
        result = Solution.count_letter_in_string(s, letter)
        assert result == expected

    def test_3(self):
        s = "hello"
        letter = "o"
        expected = 1
        result = Solution.count_letter_in_string(s, letter)
        assert result == expected


class TestZad6(unittest.TestCase):

    def test_0(self):
        n = 10
        expected = 25
        result = Solution.sum_of_odd_numbers(n)
        assert result == expected

    def test_1(self):
        n = 1
        expected = 1
        result = Solution.sum_of_odd_numbers(n)
        assert result == expected

    def test_2(self):
        n = 2
        expected = 1
        result = Solution.sum_of_odd_numbers(n)
        assert result == expected

    def test_3(self):
        n = 3
        expected = 4
        result = Solution.sum_of_odd_numbers(n)
        assert result == expected


class TestZad7(unittest.TestCase):

    def test_0(self):
        l1 = [1, 2, 3, 4]
        l2 = [2, 3, 4, 5]
        expected = [2, 3, 4]
        result = Solution.inner_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_1(self):
        l1 = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8]
        expected = []
        result = Solution.inner_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_2(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        result = Solution.inner_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_3(self):
        l1 = [1, 2, 4, 8, 10]
        l2 = [1, 2, 10, 12]
        expected = [1, 2, 10]
        result = Solution.inner_join_two_sorted_lists(l1, l2)


class TestZad8(unittest.TestCase):

    def test_0(self):
        haystack = "hello"
        needle = "l"
        expected = 2
        result = Solution.find_index_of_first_occurrence_of_element_in_string(haystack, needle)
        assert result == expected

    def test_1(self):
        haystack = "hello"
        needle = "e"
        expected = 1
        result = Solution.find_index_of_first_occurrence_of_element_in_string(haystack, needle)
        assert result == expected

    def test_2(self):
        haystack = "hello"
        needle = "h"
        expected = 0
        result = Solution.find_index_of_first_occurrence_of_element_in_string(haystack, needle)
        assert result == expected

    def test_3(self):
        haystack = "hello"
        needle = "o"
        expected = 4
        result = Solution.find_index_of_first_occurrence_of_element_in_string(haystack, needle)
        assert result == expected


class TestZad9(unittest.TestCase):

    def test_0(self):
        l1 = [1, 2, 3, 4]
        l2 = [2, 3, 4, 5]
        expected = [1, 5]
        result = Solution.outer_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_1(self):
        l1 = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = Solution.outer_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_2(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 2, 3, 4]
        expected = []
        result = Solution.outer_join_two_sorted_lists(l1, l2)
        assert result == expected

    def test_3(self):
        l1 = [1, 2, 4, 8, 10]
        l2 = [1, 2, 10, 12]
        expected = [4, 8, 12]
        result = Solution.outer_join_two_sorted_lists(l1, l2)
        assert result == expected


class TestZad10(unittest.TestCase):

    def test_0(self):
        head = Solution.ListNode(3, Solution.ListNode(2, Solution.ListNode(0, Solution.ListNode(-4))))
        head.next.next.next.next = head.next
        expected = True
        result = Solution.linked_list_cycle(head)
        assert result == expected

    def test_1(self):
        head = Solution.ListNode(1, Solution.ListNode(2))
        head.next.next = head
        expected = True
        result = Solution.linked_list_cycle(head)
        assert result == expected

    def test_2(self):
        head = Solution.ListNode(1)
        expected = False
        result = Solution.linked_list_cycle(head)
        assert result == expected

    def test_3(self):
        head = Solution.ListNode(1,
                                 Solution.ListNode(2, Solution.ListNode(3, Solution.ListNode(4, Solution.ListNode(5)))))
        expected = False
        result = Solution.linked_list_cycle(head)
        assert result == expected
