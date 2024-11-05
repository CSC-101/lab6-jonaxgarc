import data
import lab6
import unittest
from data import Book


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        book1 = Book(["Author", "Bauthor", "Cauthor", "Dauthor"], "Atitle")

        bookList = [book1]

        lab6.selection_sort_books(bookList)

        expected = [book1]
        result = bookList

        self.assertEqual(result, expected)

    def test_selection_sort_books2(self):
        book1 = Book(["James", "Sofia", "Janelle", "Max"], "Atitle")

        bookList = [book1]

        lab6.selection_sort_books(bookList)

        expected = [book1]
        result = bookList

        self.assertEqual(result, expected)

    # Part 2
    def test_swap_case1(self):
        self.assertEqual(lab6.swap_case("Your Mom"), "yOUR mOM")
    def test_swap_case2(self):
        self.assertEqual(lab6.swap_case("Your Dad"), "yOUR dAD")

    # Part 3
    def test_str_translate1(self):
        self.assertEqual(lab6.str_translate("Jonathan", "o", "0"), "J0nathan")
    def test_str_translate2(self):
        self.assertEqual(lab6.str_translate("Garcia", "a", "@"), "G@rci@")

    # Part 4
    def test_histogram1(self):
        self.assertEqual(lab6.histogram("a b a"), {"a": 2, "b": 1})
    def test_histogram2(self):
        self.assertEqual(lab6.histogram("b b a"), {"a": 1, "b": 2})

if __name__ == '__main__':
    unittest.main()
