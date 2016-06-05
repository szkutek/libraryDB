class Add:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def book(self, parameters):
        query = ("INSERT INTO books "
                 "(author_id, title, title_original, language, isbn, publish_year, publisher_id, classification_id) "
                 "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def genreToBook(self, parameters):
        query = ("CALL AddGenreToBook( %s, %s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def author(self, parameters):
        query = ("INSERT INTO authors (first_name, last_name) VALUES (%s, %s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def publisher(self, parameters):
        query = ("INSERT INTO publishers (publisher, address) VALUES (%s, %s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def classification(self, parameters):
        query = ("INSERT INTO classifications (description) VALUES (%s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def genre(self, parameters):
        query = ("INSERT INTO genres (genre) VALUES (%s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

        # def delete(self, type, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
        #
        # def deleteAll(self, type, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
        #
        # def search(self, type, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
