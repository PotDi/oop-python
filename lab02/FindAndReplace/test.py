import unittest
import replace


class TestFindAndReplace(unittest.TestCase):
    def test_replace_missing_text(self):
        self.assertEqual(replace.find_and_replace("Make love not war",
                                                  "november", "december"),
                         "Make love not war")

    def test_replace_single_occurrence(self):
        self.assertEqual(replace.find_and_replace("meat", "t", "l"), "meal")

    def test_replace_multiple_occurrence(self):
        self.assertEqual(replace.find_and_replace("to be or not to be",
                                                  "to be",
                                                  "TO BE"), "TO BE or not "
                                                            "TO BE")



if __name__ == "__main__":
    unittest.main()
