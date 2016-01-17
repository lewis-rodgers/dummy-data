import random
import webapp2

from google.appengine.ext import ndb
from google.appengine.ext import vendor
vendor.add('lib')
import markovify


with open('corpus.txt') as f:
    text = f.read()


text_model = markovify.Text(text)


def generate_paragraphs(count=1):
    paragraphs = []
    for i in xrange(count):
        paragraphs.append('<p>')
        paragraphs.append(generate_sentences(random.randint(3, 10)))
        paragraphs.append('</p>')
    return ' '.join(paragraphs)


def generate_sentences(count=1):
    sentences = []
    for i in xrange(count):
        sentences.append(text_model.make_sentence())
    return ' '.join(sentences)


class Dummy(ndb.Model):
    title = ndb.TextProperty()
    summary = ndb.TextProperty()
    body = ndb.TextProperty()
    created = ndb.StringProperty()


class DummyHandler(webapp2.RequestHandler):
    for item in xrange(10):
        e = Dummy(
            title=text_model.make_short_sentence(70),
            summary=generate_sentences(random.randint(1, 3)),
            body=generate_paragraphs(random.randint(3, 10)),
        )
        e.put()

    def get(self):
        self.response.out.write('Done')


app = webapp2.WSGIApplication([
    ('/add_data', DummyHandler)
], debug=True)