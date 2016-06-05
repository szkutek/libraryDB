class Customer:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def register(self, parameters):
        query = (
            "INSERT INTO customers (customer_barcode, name, address, birth_date, phone_no, email, registration_date) "
            "VALUES (%s, %s, %s, %s, %s, %s, curdate())")
        self.dbConnector.executeQuery(query=query, parameters=parameters)

        # def delete(self, parameters):
        #     query = ("DELETE FROM customers WHERE name LIKE '%s' AND customer_barcode = %s")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)

        # def update(self, parameters):
        #     query = (" ")
        #     self.dbConnector.executeQuery(query=query, parameters=parameters)
