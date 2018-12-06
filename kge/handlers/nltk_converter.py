from nltk import Tree

class NltkConverter:
    def __init__(self):
        pass

    @staticmethod
    def convert_token(token):
        return "_".join([token.lemma_, token.tag_, token.dep_])

    @staticmethod
    def to_nltk_tree(node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(NltkConverter.convert_token(node), [NltkConverter.to_nltk_tree(child) for child in node.children])
        else:
            return NltkConverter.convert_token(node)