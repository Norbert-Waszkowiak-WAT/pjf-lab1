class Solution:
    """
    Opracuj program, który zamieni liczbę rzymską na liczbę arabską.
    """
    @staticmethod
    def romanToInt(s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        s = s.upper()
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total

    """
    FizzBuzz
    """
    @staticmethod
    def fizzbuzz(n: int) -> list[str]:
        out: list[str] = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out

    """
    BMI = waga / (wzrost^2), zaokrąglenie do 2 miejsc.
    """
    @staticmethod
    def bmi(weight: float, height: float) -> float:
        if height == 0:
            raise ValueError("Height cannot be zero.")
        return round(weight / (height * height), 2)

    """
    Sprawdź czy liczba jest pierwsza.
    """
    @staticmethod
    def prime_number(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    """
    Policz wystąpienia litery w stringu.
    """
    @staticmethod
    def count_letter_in_string(s: str, letter: str) -> int:
        if len(letter) != 1:
            raise ValueError("letter must be a single character")
        return s.count(letter)

    """
    Zwróć sumę liczb nieparzystych od 1 do n (włącznie).
    Przykład: n=10 → 1+3+5+7+9 = 25
    """
    @staticmethod
    def sum_of_odd_numbers(n: int) -> int:
        if n <= 0:
            return 0
        k = (n + 1) // 2
        return k * k

    """
    Część wspólna (posortowana, bez duplikatów).
    """
    @staticmethod
    def inner_join_two_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
        i = j = 0
        out: list[int] = []
        while i < len(l1) and j < len(l2):
            if l1[i] == l2[j]:
                if not out or out[-1] != l1[i]:
                    out.append(l1[i])
                i += 1
                j += 1
            elif l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return out

    """
    Zwróć indeks pierwszego wystąpienia (albo -1).
    """
    @staticmethod
    def find_index_of_first_occurrence_of_element_in_string(haystack: str, needle: str) -> int:
        return haystack.find(needle)

    """
    Suma zbiorów bez części wspólnej (symetryczna różnica), posortowana i bez duplikatów.
    Dla [1,2,3,4] i [2,3,4,5] → [1,5]
    """
    @staticmethod
    def outer_join_two_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
        i = j = 0
        out: list[int] = []
        while i < len(l1) and j < len(l2):
            if l1[i] == l2[j]:
                val = l1[i]
                while i < len(l1) and l1[i] == val:
                    i += 1
                while j < len(l2) and l2[j] == val:
                    j += 1
            elif l1[i] < l2[j]:
                if not out or out[-1] != l1[i]:
                    out.append(l1[i])
                i += 1
            else:
                if not out or out[-1] != l2[j]:
                    out.append(l2[j])
                j += 1
        # dołóż ogony
        while i < len(l1):
            if not out or out[-1] != l1[i]:
                out.append(l1[i])
            i += 1
        while j < len(l2):
            if not out or out[-1] != l2[j]:
                out.append(l2[j])
            j += 1
        return out

    class ListNode:
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

    """
    Wykrywanie cyklu w liście jednokierunkowej (Floyd tortoise & hare).
    """
    @staticmethod
    def linked_list_cycle(head: "Solution.ListNode") -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
