""" Generate random, non latin, copy that looks more 'real world'

https://github.com/jsvine/markovify - Markovify is a simple, extensible Markov chain generator. Right now, its main use is for building Markov models of large corpora of text, and generating random sentences from that.
"""
import markovify
class BodyCopy(object):
    def __init__(self, text):
        self.markovify = markovify.Text(text)

    def make_sentences(self, sentence_count=1):
        """Return a list of sentences

        Args:
        char_limit (int): limit amount of characters in a sentence
        sentence_count (int): amount of sentences
        """
        results = []
        for _ in xrange(sentence_count):
            results.append(self.markovify.make_sentence())
        return results

    def make_paragraphs(self, paragraph_count=1, sentence_count=1):
        """Return a list of paragraphs

        Args:
        char_limit (int): limit amount of characters in a sentence
        paragraph_count (int): amount of paragraphs to create
        sentence_count (int): amount of sentences in a paragraph
        """
        results = []
        for _ in xrange(paragraph_count):
            results.append(
                ' '.join(self.make_sentences(sentence_count))
            )
        return results


"""Generate names

uinames.com - A simple tool to generate names for use in designs and mockups. Check the documentation for additional parameters.
"""
import urllib2
import json
class UserName:
    def __init__(self, amount=1, **kwargs):
        self.uri = 'http://api.uinames.com/?%s' % amount

    def make_names(self):
        return json.load(urllib2.urlopen(self.uri))
