class Book:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def rentBook(self, parameters):
        query = ("CALL RentBook(%s, %s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def returnBook(self, parameters):
        query = ("CALL ReturnBook(%s);")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

        # def renew(self, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
