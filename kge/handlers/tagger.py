import spacy, json
from spacy.symbols import ORTH, POS, NOUN
from kge.handlers import NltkConverter

class Tagger:
    def __init__(self):
        self.spacy = spacy.load('en')
        self.spacy.add_pipe(Tagger.one_sentence_per_doc, before='parser')
        with open('data/lemmas.json', 'r') as fp:
            self.lemmas = set(json.load(fp))

        key_tokens = {
            'expr': NOUN
        }
        for key_token in key_tokens:
            for i in range(5):
                token = f'{key_token}{i}'
                print(f'Adding token {token} as {key_tokens[key_token]}...')
                self.spacy.tokenizer.add_special_case(token, [{ORTH: token, POS: key_tokens[key_token]}])

    @staticmethod
    def one_sentence_per_doc(doc):
        if len(doc) <= 1:
            return doc

        doc[0].sent_start = True
        for i in range(1, len(doc)):
            doc[i].sent_start = False
        return doc

    def flatten_token(self, sent):
        ntok_list = []
        for token in sent:
            token_text, token_pos = (token.lemma_, 'POS') if token.lemma_ in self.lemmas else ('text', token.pos_)
            ntok_list.append(f"{token_text}_{token_pos}")
        return ntok_list

    def parse(self, text):
        doc = self.spacy(text)
        sent = [sent for sent in doc.sents][0]
        NltkConverter.to_nltk_tree(sent.root).pretty_print()
        return self.flatten_token(sent), sent