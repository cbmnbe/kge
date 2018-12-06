from kge import providers

def callback(data):
    assert data is not None

def test_execute():
    provider = providers.NeoProvider()
    provider.execute('MATCH (cloudAtlas {title: "Cloud Atlas"}) RETURN cloudAtlas', callback)