class Data:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def parse(self, cmd, parameters):
        if cmd == '':
            self.add(parameters)
        elif cmd == '': 
            self.update(parameters)
        elif cmd == '':
            self.delete(parameters)

    def add(self, type, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def update(self, type, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def delete(self, type, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def deleteAll(self, type, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def search(self, type, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)
