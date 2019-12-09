import preprocessing
import unittest

class TestPreprocessing(unittest.TestCase):

    def test_tokenize(self):
        input_string = "Hello, this is a sentence."
        result = preprocessing.tokenize(input_string)
        expected = ["Hello", ",", "this", "is", "a", "sentence", "."]
        self.assertEqual(result, expected)

    def test_compute_labels(self):
        long_text =  ["a", "b", "c", "d", "a", "b"]
        short_text = ["a",      "c",      "a", "b"]
        result = preprocessing.compute_labels(long_text, short_text)
        expected = [1, 0, 1, 0, 1, 1]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
