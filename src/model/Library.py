from Customer import Customer
from Query import Query
from Book import Book
from Add import Add


class Library:
    def __init__(self, dbC):
        self.dbConnector = dbC
        self.customer = Customer(dbc=dbC)
        self.query = Query(dbc=dbC)
        self.add = Add(dbc=dbC)
        self.book = Book(dbc=dbC)
        self.dbConnector.connect()

