import unittest
import markovify
from dummy_data import BodyCopy


class BodyCopyTest(unittest.TestCase):

    def setUp(self):
        with open('corpus.txt') as f:
            text = f.read()
        self.model = BodyCopy(text)

    def test_make_sentences(self):
        sen = self.model.make_sentences(sentence_count=2)
        assert(len(sen) == 2)

    def test_make_paragraphs(self):
        para = self.model.make_paragraphs(paragraph_count=2)
        assert(len(para) == 2)


if __name__ == '__main__':
    unittest.main()
