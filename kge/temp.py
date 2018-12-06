from kge import providers
from kge import handlers
from kge import interfacers

def get_field(data):
    for record in data:
        for key in record.keys():
            return record[key]

text = 'Get my pnl'
print(text)
converter = handlers.TempConverter()
cypher_query = converter.convert(text)
print(cypher_query)

provider = providers.NeoProvider()
data = provider.execute(cypher_query)
command = get_field(data)
print(command)

interfacer = interfacers.PythonInterfacer()
interfacer.execute(command)
