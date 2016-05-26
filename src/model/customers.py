class Customer:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def parse(self, cmd, parameters):
        if cmd == 'register':
            self.register(parameters)

    def register(self, parameters):
        query = (
            "INSERT INTO customers (customer_barcode, name, address, birthdate, phone_no, email, registration_date) "
            "VALUES (%s, %s, %s, %s, %s, %s, NOW())")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def delete(self, parameters):
        query = ("DELETE FROM customers WHERE name REGEXP '%s' AND customer_barcode REGEXP '%s'")
        # query = ("DELETE FROM customer WHERE name LIKE '%%s%' AND customer_barcode LIKE '%%s%'")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

    def deleteAll(self):
        query = ("DELETE FROM customers")
        # self.dbConnector.executeQuery(query=query, parameters=parameters)

    def simpleSearch(self, parameters):
        query = ("SELECT * FROM customers WHERE name LIKE '%s'")
        return self.dbConnector.searchQuery(query=query, parameters=parameters)

    def advancedSearch(self, parameters):
        query = (" ")
        return self.dbConnector.searchQuery(query=query, parameters=parameters)

    def update(self, parameters):
        query = (" ")
        self.dbConnector.executeQuery(query=query, parameters=parameters)
