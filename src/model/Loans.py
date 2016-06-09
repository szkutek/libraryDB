class Loans:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def rentBook(self, parameters):
        # customerBarcode = parameters[0]
        volumeBarcode = parameters[1]
        available = "SELECT volume_id FROM volumes JOIN available_volumes USING (volume_id) WHERE barcode = %s;"
        cursor = self.dbConnector.searchQuery(query=available, parameters=(volumeBarcode,), multi=False)
        if cursor.fetchone() is None:
            return 'Could not rent.'
        else:
            self.dbConnector.callProcedure('RentBook', parameters=parameters)
            return 'Successfully rented.'

    def returnBook(self, parameters):
        volumeBarcode = parameters[0]
        notavailable = """SELECT volume_id
                            FROM volumes
                            WHERE volume_id NOT IN (SELECT volume_id
                                                    FROM available_volumes)
                                  AND volumes.barcode = %s;"""
        cursor = self.dbConnector.searchQuery(query=notavailable, parameters=(volumeBarcode,), multi=False)
        if cursor.fetchone() is None:
            return 'Could not return.'
        else:
            self.dbConnector.callProcedure('ReturnBook', parameters=parameters)
            return 'Successfully returned.'

            # def renew(self, parameters):
            #     query = (" ")
            #     self.dbConnector.executeQuery(query=query, parameters=parameters)
