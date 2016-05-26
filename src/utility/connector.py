import mysql.connector


class DBConnector:
    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(user=self.user, password=self.password, database=self.database)

    def close(self):
        self.connection.close()

    def executeQuery(self, query, parameters):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        self.connection.commit()
        cursor.close()

    def searchQuery(self,query,parameters):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        # self.connection.commit()
        return cursor
