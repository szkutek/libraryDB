from customers import Customer
from AdvQueries import AdvQuery


class Library:
    def __init__(self, dbC):
        self.dbConnector = dbC
        self.customer = Customer(dbc=dbC)
        self.advQuery = AdvQuery(dbc=dbC)
        self.dbConnector.connect()

    def parseCommand(self, cmd, parameters):
        self.customer.parse(cmd=cmd, parameters=parameters)

    def run(self):
        # comunicate
        self.parseCommand('', '')
