class Add:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def book(self, parameters):
        # in param = author name, surname, title, title_orig, language, isbn, publish_year, publisher, class
        # query = ("CALL AddBook( %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        # self.dbConnector.executeQuery(query=query, parameters=parameters)
        self.dbConnector.callProcedure('AddBook', parameters=parameters)

    def genreToBook(self, parameters):
        # query = ("CALL AddGenreToBook( %s, %s);")
        # self.dbConnector.executeQuery(query=query, parameters=parameters)
        self.dbConnector.callProcedure('AddGenreToBook', parameters=parameters)

    def volume(self, parameters):
        # query = ("CALL AddVolume(%s, %s) ") # volume_barcode, isbn
        self.dbConnector.callProcedure('AddVolume', parameters=parameters)

    def author(self, parameters):
        query = "INSERT INTO `authors` (first_name, last_name) VALUES (%s, %s);"
        self.dbConnector.executeQuery(query=query, parameters=parameters, multi=False)

    def publisher(self, parameters):
        query = "INSERT INTO publishers (publisher, address) VALUES (%s, %s);"
        self.dbConnector.executeQuery(query=query, parameters=parameters, multi=False)

    def classification(self, parameters):
        query = "INSERT INTO classifications (description) VALUES (%s);"
        self.dbConnector.executeQuery(query=query, parameters=parameters, multi=False)

    def genre(self, parameters):
        query = "INSERT INTO genres (genre) VALUES (%s);"
        self.dbConnector.executeQuery(query=query, parameters=parameters, multi=False)

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
