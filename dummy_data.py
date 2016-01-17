import markovify


class BodyCopy(markovify.Text):
    def generate_paragraph(self, para_count=1, sen_count=1):
        results = []
        for i in xrange(para_count):
            results.append(
                ' '.join(self.generate_sentence(sen_count))
            )
        return results

    def generate_sentence(self, sen_count=1):
        results = []
        for i in xrange(sen_count):
            results.append(self.make_sentence())
        return results
