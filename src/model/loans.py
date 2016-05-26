class Loan:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def parse(self, cmd, parameters):
        if cmd == '':
            self.checkOut(parameters)
        elif cmd == '':
            self.checkIn(parameters)
        elif cmd == '':
            self.renew(parameters)

    def checkOut(self, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def checkIn(self, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def renew(self, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)
