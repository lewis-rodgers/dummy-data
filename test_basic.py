import unittest
from dummy_data import BodyCopy


class BodyCopyTest(unittest.TestCase):

    def setUp(self):
        with open('corpus.txt') as f:
            self.text = f.read()
        self.text_model = BodyCopy(self.text)

    def test_generate_paragraph(self):
        para = self.text_model.generate_paragraph(2)
        assert(len(para) == 2)

    def test_generate_sentence(self):
        sen = self.text_model.generate_sentence(2)
        assert(len(sen) == 2)


if __name__ == '__main__':
    unittest.main()
