from kge import handlers

def test_locate():
    locator = handlers.QuestionLocator()
    cases = {
        'Can you please plot my pnl for the last 3 years?' : 'Can you please plot my pnl for the last 3 years?'
    }
    for case in cases:
        located = locator.locate(case)
        assert located == cases[case]