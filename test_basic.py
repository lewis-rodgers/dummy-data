import unittest
from dummy_data import BodyCopy


class BodyCopyTest(unittest.TestCase):

    def setUp(self):
        self.text_model = BodyCopy()

    def test_make_paragraphs(self):
        para = self.text_model.make_paragraphs(paragraph_count=2)
        assert(len(para) == 2)

    def test_make_sentences(self):
        sen = self.text_model._make_sentences(sentence_count=2)
        assert(len(sen) == 2)


if __name__ == '__main__':
    unittest.main()
