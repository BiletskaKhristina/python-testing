import unittest
from unittest.mock import patch

from app import Figure, count_vowels, get_number


class TestFigure(unittest.TestCase):

    def test_square(self):
        figure = Figure("квадрат", 5)
        self.assertEqual(figure.get_figure_type(), "квадрат")
        self.assertEqual(figure.get_figure_length(), 20)
        self.assertEqual(figure.get_angles(), [90, 90, 90, 90])

    def test_rectangle(self):
        figure = Figure("прямокутник", 4)
        self.assertEqual(figure.get_figure_length(), 8)
        self.assertEqual(figure.get_angles(), [90, 90, 90, 90])

    def test_triangle(self):
        figure = Figure("трикутник", 3)
        self.assertEqual(figure.get_figure_length(), 9)
        self.assertEqual(figure.get_angles(), [60, 60, 60])

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            Figure("коло", 5)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)

    def test_subtest_lengths(self):
        for length in [1, 5, 10]:
            with self.subTest(length=length):
                figure = Figure("квадрат", length)
                self.assertEqual(figure.get_figure_length(), length * 4)


class TestVowels(unittest.TestCase):

    def test_ukrainian_word(self):
        self.assertEqual(count_vowels("Україна"), 4)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_numbers(self):
        self.assertEqual(count_vowels("12345"), 0)

    def test_english_word(self):
        self.assertEqual(count_vowels("hello"), 2)


class TestInput(unittest.TestCase):

    @patch("builtins.input", return_value="5")
    def test_get_number(self, mock_input):
        self.assertEqual(get_number(), 5)
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="-2")
    def test_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            get_number()


if __name__ == "__main__":
    unittest.main()

