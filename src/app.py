from utility.connector import DBConnector
from model.customers import Customer
import datetime


class Library:
    def __init__(self, dbC):
        self.dbConnector = dbC
        self.customer = Customer(dbc=dbC)
        self.dbConnector.connect()

    def parseCommand(self, cmd, parameters):
        self.customer.parse(cmd=cmd, parameters=parameters)

    def run(self):
        # comunicate
        self.parseCommand('', '')


lib = Library(DBConnector(user='root', password='root1234', database='library'))
lib.parseCommand(cmd='register',
                 parameters=(00000001, 'Sebastian', 'a', datetime.date(1994, 10, 20), '1234', 'bla@bla.com'))
