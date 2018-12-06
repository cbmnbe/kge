from kge import providers

def test_normalize():
    normalizer = providers.DataNormalizer()
    normalized = normalizer.normalize(None)
    assert normalized == None