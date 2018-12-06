import json

with open('data/templates.json', 'r') as fp:
    templates = json.load(fp)

while True:
    sentence = input('Sentence:')
    template = input('Cypher query:')
    context = "main"
    templates.append({
        'sentence': sentence,
        'template': template,
        'context': context
    })

    with open('data/templates.json', 'w') as fp:
        fp.write(json.dumps(templates, indent=4))
    print('Written.')