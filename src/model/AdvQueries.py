class AdvQuery:
    def __init__(self, dbc):
        self.dbConnector = dbc

    # def parse(self, cmd, parameters):
    #

    def simple(self, parameters):  # author and title only
        results = []
        for i in parameters:
            query = (
                "SELECT authors.name AS author, title, language, publish_year, isbn, publishers.name AS publisher"
                "FROM books JOIN book_authors USING (book_id)"
                "JOIN authors ON book_authors.author_id = authors.author_id"
                "JOIN publishers ON publishers.publisher_id = books.publisher_id"
                "WHERE authors.name REGEXP '%s' OR title REGEXP '%s'")
            res = self.dbConnector.searchQuery(query=query, parameters=parameters[i])
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
