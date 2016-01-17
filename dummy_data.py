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


# # Usage
# with open('../corpus.txt') as f:
#     text = f.read()


# copy = BodyCopy(text)


# # Generates a list of 2 sentences
# print(copy.generate_sentence(2))

# # Generates a list of 2 paragraphs. Each paragraph is 2 sentences in length.
# print(copy.generate_paragraph(2, 2))
