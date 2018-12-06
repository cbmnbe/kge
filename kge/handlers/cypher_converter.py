import nltk, json
from pprint import pprint

class CypherConverter:
    def __init__(self):
        with open('data/lemmas.json', 'r') as fp:
            self._useless = set([f"{word}_POS" for word in json.load(fp)])
        self._useless.add('text_DET')

    def convert_rec(self, node, tokens, literrals):
        if type(node) is not nltk.Tree:
            index = len(literrals)
            literral = {
                'type': 'literral',
                'literral' : f"{node}",
                'index': index,
                'text' : tokens[index].text,
                'children': [],
                'children_count': 0
            }
            literrals.append(literral)
            if node in self._useless:
                return None
            return literral
        
        node_infos = {
            'type': node.label()
        }

        children = []
        for child in node: 
            child_info = self.convert_rec(child, tokens, literrals)
            if child_info is not None:
                children.append(child_info)
        node_infos['children_count'] = len(children)
        node_infos['children'] = children

        return node_infos

    def minimize_rec(self, node_info):
        if node_info['type'] == 'RAW_ITEM':
            return node_info['children'][0]['text']

        if node_info['type'] == 'REL':
            item1 = self.minimize_rec(node_info['children'][0])
            item2 = self.minimize_rec(node_info['children'][2])
            rel = node_info['children'][1]['text']
            return f"({item1}) -[:{rel}]> ({item2})"

        if node_info['type'] == 'OR_ITEM':
            item1 = self.minimize_rec(node_info['children'][0])
            item2 = self.minimize_rec(node_info['children'][1])
            return f"{item1}, {item2}"

        if node_info['type'] == 'AND_ITEM':
            item1 = self.minimize_rec(node_info['children'][0])
            item2 = self.minimize_rec(node_info['children'][1])
            return f"{item1}, {item2})"

        if node_info['type'] == 'PROP_ITEM':
            item1 = self.minimize_rec(node_info['children'][0])
            item2 = self.minimize_rec(node_info['children'][1])
            return f"({item1}) WHERE {item2}"

        stri = ""
        for child in node_info['children']:
            stri += self.minimize_rec(child)
        
        return stri

    def convert(self, cfg_parsed, sent):
        print(cfg_parsed)
        literrals = []
        node_info = self.convert_rec(cfg_parsed, [token for token in sent], literrals)
        print(json.dumps(node_info, indent=4))
        minimized = self.minimize_rec(node_info)
        print(minimized)
        return 'sas'