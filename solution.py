class Solution:
    """
    Opracuj program, który zamieni liczbę rzymską na liczbę arabską.
    Przykład:
    Input: s = "III"
    Output: 3
    """
    @staticmethod
    def romanToInt(s: str) -> int:
        pass

    """
    Opracuj program FizzBuzz, który zwróci liste stringów od 1 do n.
    Dla każdego elementu z listy:
    - jeśli liczba jest podzielna przez 3 zamiast liczby zwróci "Fizz"
    - jeśli liczba jest podzielna przez 5 zamiast liczby zwróci "Buzz"
    - jeśli liczba jest podzielna przez 3 i 5 zamiast liczby zwróci "FizzBuzz"

    Przykład:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    """
    @staticmethod
    def fizzbuzz(n: int) -> list[str]:
        pass

    """
    Opracuj program, który obliczy BMI na podstawie wagi i wzrostu.
    BMI = waga / (wzrost^2)
    Wynik zaokrąglij do 2 miejsc po przecinku.

    Przykład:
    Input: weight = 70, height = 1.75
    Output: 22.86
    """
    @staticmethod
    def bmi(weight: float, height: float) -> float:
        pass

    """
    Opracuj program, który sprawdzi czy podana liczba jest liczbą pierwszą.
    Liczba pierwsza to taka liczba, która jest podzielna przez 1 i samą siebie.

    Przykład:
    Input: n = 7
    Output: True
    """
    @staticmethod
    def prime_number(n: int) -> bool:
        pass

    """
    Opracuj program, który zliczy ile razy litera występuje w podanym stringu.

    Przykład:
    Input: s = "hello", letter = "l"
    Output: 2
    """
    @staticmethod
    def count_letter_in_string(s: str, letter: str) -> int:
        pass

    """
    Opracuj program, który zwróci sumę liczb nieparzystych z podanej listy.

    Przykład:
    Input: n = 10
    Output: 25
    """
    @staticmethod
    def sum_of_odd_numbers(n: int) -> int:
        pass

    """
    Opracuj program, który z dwóch podanych list zwróci jedną posortowaną listę, która będzie 
    zawierała liczby wyłącznie występujące w obu listach.

    Przykład:
    Input: l1 = [1,2,3,4], l2 = [2,3,4,5]
    Output: [2,3,4]
    """
    @staticmethod
    def inner_join_two_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
        pass

    """
    Opracuj program, który zwróci indeks pierwszego wystąpienia elementu w stringu lub -1 jeśli
    element nie występuje.

    Przykład:
    Input: haystack = "hello", needle = "l"
    Output: 2

    Input: haystack = "hello", needle = "g"
    Output: -1
    """
    @staticmethod
    def find_index_of_first_occurrence_of_element_in_string(haystack: str, needle: str) -> int:
        pass

    """
    Opracuj program, który z dwóch podanych list zwróci jedną posortowaną listę, która będzie
    zawierała niepowtarzające się elementy z obu list.

    Przykład:
    Input: l1 = [1,2,3,4], l2 = [2,3,4,5]
    Output: [1,5]
    """

    @staticmethod
    def outer_join_two_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
        pass

    class ListNode:
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

    """
    Biorąc pod uwagę "head", nagłówek połączonej listy, określ, czy linked lista ma w sobie cykl.
    Cykl na linked liście występuje, jeśli na liście znajduje się węzeł, do którego można ponownie dotrzeć poprzez ciągłe podążanie za następnym wskaźnikiem. 
    Wewnętrznie, "pos" jest używane do oznaczenia indeksu węzła, z którym połączony jest następny wskaźnik tail. Zauważ, że pos nie jest przekazywane jako parametr.
    Zwraca wartość true, jeśli na połączonej liście istnieje cykl. W przeciwnym razie zwraca false.

    Przykład:

    Input: head = [3,2,0,-4], pos = 1, Patrz obrazek "linked_list_cycle1.png"
    Output: True
    Wyjaśnienie: Cykl zaczyna się na drugim elemencie listy i wygląda następująco: 3 -> 2 -> 0 -> -4 -> 2

    Input: head = [1,2], pos = 0, Patrz obrazek "linked_list_cycle2.png"
    Output: True
    Wyjaśnienie: Cykl zaczyna się na pierwszym elemencie listy i wygląda następująco: 1 -> 2 -> 1

    Input: head = [1], pos = -1, Patrz obrazek "linked_list_cycle3.png"
    Output: False
    Wyjaśnienie: W liście nie ma cyklu.
    """
    @staticmethod
    def linked_list_cycle(head: ListNode) -> bool:
        pass
