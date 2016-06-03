import datetime






lib.parseCommand(cmd='register',
                 parameters=(00000005, 'Sebastian', 'a', datetime.date(1994, 10, 20), '1234', 'bla@bla.com'))

cursor = lib.advQuery.advanced(parameters=('asi', 'asi', 'found', 1970, 's', '12345'))
for (author, title, publish_year, language, publisher, available) in cursor:
    print(
        str(author) + ',' + str(title) + ',' + str(publish_year) + ',' + str(language) + ',' + str(
            publisher) + ',' + str(available))
