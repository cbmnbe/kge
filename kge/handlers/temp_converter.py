import json
import spacy

class TempConverter:
    def __init__(self):
        with open('data/templates.json') as fp:
            self._templates = json.load(fp)
        self._nlp = spacy.load('en')

        self._template_docs = [{
            'sentence': template['sentence'],
            'doc': self._nlp(template['sentence'])
        } for template in self._templates]

    def _tune_template(self, text, index):
        return self._templates[index]['template']

    def convert(self, text):
        text_doc = self._nlp(text)
        max_similarity = 0.0
        max_template_index = -1
        for index, template in enumerate(self._template_docs):
            similarity = template['doc'].similarity(text_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                max_template_index = index

        return None if max_template_index < -1 else self._tune_template(text, max_template_index)