from utility.connector import DBConnector
from model.customers import Customer
from model.AdvQueries import AdvQuery
import datetime


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


lib = Library(DBConnector(user='root', password='root1234', database='library'))

lib.parseCommand(cmd='register',
                 parameters=(00000005, 'Sebastian', 'a', datetime.date(1994, 10, 20), '1234', 'bla@bla.com'))

cursor = lib.advQuery.advanced(parameters=('asi', 'asi', 'found', 1970, 's', '12345'))
for (author, title, publish_year, language, publisher, available) in cursor:
    print(
        str(author) + ',' + str(title) + ',' + str(publish_year) + ',' + str(language) + ',' + str(
            publisher) + ',' + str(available))
