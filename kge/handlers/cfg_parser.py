import nltk

class CfgParser:
    def __init__(self):
        with open('data/grammar.cfg') as fp:
            self._grammar = nltk.CFG.fromstring(fp.read())

    def parse(self, ntok_list):
        print(ntok_list)
        rd_parser = nltk.BottomUpLeftCornerChartParser(self._grammar)
        tree = [tree for tree in rd_parser.parse(ntok_list)][0]
        return tree
