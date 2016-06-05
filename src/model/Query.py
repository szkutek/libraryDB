class Query:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def simple(self, parameters):  # author and title only
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
        query = (
            "SELECT "
            "last_name author,"
            "title,"
            "publish_year,"
            "language,"
            "publisher,"
            "COUNT(volume_id) available "
            "FROM books "
            "JOIN authors USING (author_id) "
            "JOIN available_volumes ON books.book_id = available_volumes.book_id "
            "JOIN publishers USING (publisher_id) "
            "WHERE (last_name REGEXP %s OR first_name REGEXP %s)"
            "AND title REGEXP %s "
            "AND publish_year = %s "
            "AND publisher REGEXP %s "
            "AND isbn = %s; ")

        res = self.dbConnector.searchQuery(query=query, parameters=parameters)
        return res

    def newBooks(self, parameters):
        query = (" ")

    def popularBooks(self, parameters):
        query = (" ")
