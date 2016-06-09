class Query:
    def __init__(self, dbc):
        self.dbConnector = dbc

    def simple(self, parameters):  # author and title only
        queries = parameters[0]
        lang = parameters[1]
        year1 = parameters[2]
        year2 = parameters[3]
        self.dbConnector.callProcedure('CreateSearchTmp', parameters=(lang, year1, year2))

        results = set()
        for i in queries:
            self.dbConnector.callProcedure('SimpleSearch', parameters=(i,))
            res = self.dbConnector.get_results()
            for k in res:
                for x in k.fetchall():
                    tmp = str(x[0]) + ';' + str(x[1]) + ';' + str(x[2]) + ';' + str(x[3])
                    results.add(tmp)
        return results

    def advanced(self, parameters):
        self.dbConnector.callProcedure('AdvancedSearch', parameters=parameters)
        results = set()
        res = self.dbConnector.get_results()
        for k in res:
            for x in k.fetchall():
                tmp = str(x[0]) + ';' + str(x[1]) + ';' + str(x[2]) + ';' + str(x[3]) + ';' + str(x[4]) + ';' + str(
                    x[5])
                print(tmp)
                results.add(tmp)
        return results

    def newBooks(self, parameters):
        self.dbConnector.callProcedure('NewBooks', parameters=parameters)
        results = set()
        res = self.dbConnector.get_results()
        for k in res:
            for x in k.fetchall():
                tmp = str(x[0]) + ';' + str(x[1]) + ';' + str(x[2]) + ';' + str(x[3])
                print(tmp)
                results.add(tmp)
        return results

    def popularBooks(self, parameters):
        self.dbConnector.callProcedure('PopularBooks', parameters=parameters)
        results = set()
        res = self.dbConnector.get_results()
        for k in res:
            for x in k.fetchall():
                tmp = str(x[0]) + ';' + str(x[1]) + ';' + str(x[2])
                print(tmp)
                results.add(tmp)
        return results
