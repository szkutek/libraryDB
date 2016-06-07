class Query:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def simple(self, parameters):  # author and title only <-popr.
        results = []
        for i in parameters:
            query = (
                "CALL SimpleSearch('English', 1970, 1970);"
                "SELECT "
                "   CONCAT_WS(', ', last_name, first_name) AS author,"
                "   title,"
                "   publish_year,"
                "   available"
                "FROM SimpleSearchTemp"
                "   WHERE last_name REGEXP @zapytanie"
                "           OR first_name REGEXP @zapytanie"
                "           OR title REGEXP @zapytanie"
                "           OR title_original REGEXP @zapytanie;")
            res = self.dbConnector.searchQuery(query=query, parameters=parameters[i], multi=True)
            for k in res:
                results.append(k)
        return results

    def advanced(self, parameters):
        query = ("")
        res = self.dbConnector.searchQuery(query=query, parameters=parameters)
        return res

    def newBooks(self, parameters):
        query = (" ")

    def popularBooks(self, parameters):
        query = (" ")
