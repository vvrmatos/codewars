import unittest
from app.main import is_uppercase


class TestIsUppercase(unittest.TestCase):
    def test_all_uppercase(self):
        self.assertTrue(is_uppercase("HELLO WORLD"))
        self.assertTrue(is_uppercase("THIS IS A TEST"))

    def test_mixed_case(self):
        self.assertFalse(is_uppercase("Hello World"))
        self.assertFalse(is_uppercase("tHiS Is A tEsT"))

    def test_numbers_and_symbols(self):
        self.assertTrue(is_uppercase("12345"))
        self.assertTrue(is_uppercase("!@#$%"))
        self.assertTrue(is_uppercase("12345 !@#$%"))

    def test_empty_string(self):
        self.assertFalse(is_uppercase(""))

    def test_single_space_string(self):
        self.assertTrue(is_uppercase(" "))

    def test_mixed_alphanumeric(self):
        self.assertTrue(is_uppercase("HELLO123"))
        self.assertFalse(is_uppercase("Hello123"))

    def test_non_alpha_blocks(self):
        self.assertTrue(is_uppercase("HELLO 123 WORLD"))
        self.assertTrue(is_uppercase("THIS IS A TEST!!!"))
        self.assertFalse(is_uppercase("This IS A Test 123"))

    def test_string_with_spaces(self):
        self.assertTrue(is_uppercase("   "))
        self.assertTrue(is_uppercase("  HELLO  WORLD   "))
        self.assertFalse(is_uppercase("  Hello  World   "))


if __name__ == "__main__":
    unittest.main()
