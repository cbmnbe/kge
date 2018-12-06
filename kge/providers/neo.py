from neo4j import GraphDatabase

class NeoProvider:
    def __init__(self):
        self._uri = "bolt://localhost:7687"
        self._driver = GraphDatabase.driver(self._uri, auth=("neo4j", "neo4jpass"))
        self._current_results = None

    def query(self, tx, cypher_query):
        self._current_results = tx.run(cypher_query)

    def execute(self, cypher_query):
        with self._driver.session() as session:
            session.read_transaction(self.query, cypher_query)
        return self._current_results