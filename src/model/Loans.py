class Loans:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def rentBook(self, parameters):
        self.dbConnector.callProcedure('RentBook', parameters=parameters)

    def returnBook(self, parameters):
        # query = ("CALL ReturnBook(%s);")
        self.dbConnector.callProcedure('ReturnBook', parameters=parameters)

        # def renew(self, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
