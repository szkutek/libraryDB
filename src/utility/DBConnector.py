import mysql.connector
import time


class DBConnector:
    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def connect(self):
        self.connection = mysql.connector.connect(user=self.user, password=self.password, database=self.database)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def callProcedure(self, name, parameters):
        try:
            print("calling " + name + " with " + repr(parameters))
            self.cursor.callproc(name, args=parameters)
            # self.connection.commit()
        except Exception as e:
            print(e)

    def get_results(self):
        return self.cursor.stored_results()

    def executeQuery(self, query, parameters, multi):
        # query, parameters, multi
        try:
            print("calling " + query + " with " + repr(parameters))
            self.cursor.execute(query, parameters, multi)
            self.connection.commit()
        except Exception as e:
            print(e)

    def searchQuery(self, query, parameters, multi):
        searchCursor = self.connection.cursor()
        searchCursor.execute(query, parameters, multi)
        # self.connection.commit()
        return searchCursor
