""" Generate random copy that looks more 'real world' than lorem ipsum text

https://github.com/jsvine/markovify - Markovify is a simple, extensible Markov chain generator. Right now, its main use is for building Markov models of large corpora of text, and generating random sentences from that.
"""
import markovify
        """Place seed text in corpus.txt file

        Tip:
            Include words related to the project sponsor's industry. More text means more variety in final output.
        """

class BodyCopy(markovify.Text):
    def generate_paragraph(self, para_count=1, sen_count=1):
        """Return a list of paragraphs

        Args:
            char_limit (int): limit amount of characters in a sentence
            paragraph_count (int): amount of paragraphs to create
            sentence_count (int): amount of sentences in a paragraph
        """
        results = []
        for i in xrange(para_count):
            results.append(
                ' '.join(self.generate_sentence(sen_count))
            )
        return results

    def generate_sentence(self, sen_count=1):
        """Return a list of sentences

        Args:
            char_limit (int): limit amount of characters in a sentence
            sentence_count (int): amount of sentences
        """
        results = []
        for i in xrange(sen_count):
            results.append(self.make_sentence())
        return results
""" Generate names

uinames.com - A simple tool to generate names for use in designs and mockups. Check the documentation for additional parameters.
"""
