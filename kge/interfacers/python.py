import pandas as pd

class PythonInterfacer:
    def __init__(self):
        pass

    def execute(self, command):
        return pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/' +
            '5d1ea79569ed194d432e56108a04d188/raw/' +
            'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
            'gdp-life-exp-2007.csv')