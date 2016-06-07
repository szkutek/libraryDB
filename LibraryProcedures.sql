# SIMPLE SEARCH
DROP PROCEDURE IF EXISTS CreateSearchTemp;
CREATE PROCEDURE CreateSearchTemp(IN lang VARCHAR(20), IN year1 INT(4), IN year2 INT(4))
  BEGIN
    CREATE TEMPORARY TABLE IF NOT EXISTS SearchTemp (
      search_id      INT          NOT NULL AUTO_INCREMENT,
      first_name     VARCHAR(50)  NOT NULL,
      last_name      VARCHAR(50)  NOT NULL,
      title          VARCHAR(100) NOT NULL,
      title_original VARCHAR(100),
      publish_year   INT(4)       NOT NULL,
      available      INT          NOT NULL,
      PRIMARY KEY (search_id)
    );
    TRUNCATE SearchTemp;

    INSERT INTO SearchTemp (first_name, last_name, title, title_original, publish_year, available)
      SELECT
        first_name,
        last_name,
        title,
        title_original,
        publish_year,
        COUNT(volume_id) available
      FROM books
        JOIN authors USING (author_id)
        JOIN available_volumes ON books.book_id = available_volumes.book_id
      WHERE books.language = lang
            AND (books.publish_year BETWEEN year1 AND year2)
      GROUP BY books.book_id;
  END;

CALL CreateSearchTemp('English', 1970, 1970);

DROP PROCEDURE IF EXISTS SimpleQuery;
CREATE PROCEDURE SimpleQuery(query VARCHAR(50))
  BEGIN
    SELECT
      CONCAT_WS(', ', last_name, first_name) AS author,
      title,
      publish_year,
      available
    FROM SearchTemp
    WHERE last_name REGEXP query
          OR first_name REGEXP query
          OR title REGEXP query
          OR title_original REGEXP query;
  END;
CALL SimpleQuery('asimov');

DROP PROCEDURE IF EXISTS SimpleSearch;
CREATE PROCEDURE SimpleSearch(query VARCHAR(50))
  BEGIN
    
  END;





# WYPOŻYCZANIE KSIĄŻEK
DROP PROCEDURE IF EXISTS RentBook;
CREATE PROCEDURE RentBook(cust_barc INT(8), vol_barc INT(8))
  BEGIN
    # potrzebujemy id
    SELECT @customer_id := customer_id
    FROM customers
    WHERE customer_barcode = cust_barc;
    # pobieramy id
    SELECT @volume_id := volume_id
    FROM volumes
    WHERE barcode = vol_barc;
    # wypożyczamy
    INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
    VALUES (@customer_id, @volume_id, curdate(), ADDDATE(curdate(), 30), NULL);
    COMMIT;
  END;
CALL RentBook(1, 1);
SELECT *
FROM loans;

# ODDAWANIE KSIĄŻEK
DROP PROCEDURE IF EXISTS ReturnBook;
CREATE PROCEDURE ReturnBook(volume_barcode INT(8))
  BEGIN
    # pobieramy id
    SELECT @volume_id := volume_id
    FROM volumes
    WHERE barcode = volume_barcode;
    # zwracamy książkę
    UPDATE loans
    SET return_date = curdate()
    WHERE volume_id = @volume_id;
    COMMIT;
  END;

CALL ReturnBook(2);
SELECT *
FROM loans;

# DODAWANIE KSIĄŻKI
DROP PROCEDURE IF EXISTS AddBook;
CREATE PROCEDURE AddBook(a1 VARCHAR(50), a2 VARCHAR(50), t VARCHAR(100), t_o VARCHAR(100), l VARCHAR(20),
                         i  INT, p_y INT, p VARCHAR(50), c VARCHAR(20))
  BEGIN
    SELECT @a_id := author_id
    FROM authors
    WHERE first_name LIKE a1 AND last_name LIKE a2;
    SELECT @p_id := publisher_id
    FROM publishers
    WHERE publisher LIKE p;
    SELECT @c_id := classification_id
    FROM classifications
    WHERE description LIKE c;
    INSERT INTO books
    (author_id, title, title_original, language, isbn, publish_year, publisher_id, classification_id)
    VALUES (@a_id, t, t_o, l, i, p_y, @p_id, @c_id);
    COMMIT;
  END;

# DODAWANIE GENRE DO KSIĄŻKI
DROP PROCEDURE IF EXISTS AddGenreToBook;
CREATE PROCEDURE AddGenreToBook(i INT, g VARCHAR(20))
  BEGIN
    # potrzebujemy id
    SELECT @g_id := genre_id
    FROM genres
    WHERE genre LIKE g;
    # search for book_id
    SELECT @b_id := book_id
    FROM books
    WHERE isbn = i;
    # dodajemy do book_genres
    INSERT INTO book_genres
    (book_id, genre_id)
    VALUES (@b_id, @g_id);
    COMMIT;
  END;
# CALL AddGenreToBook(2, 'detective novel'); # WYKONYWANE W PĘTLI DLA KAŻDEGO WYBRANEGO GENRE

# ADD VOLUME
DROP PROCEDURE IF EXISTS AddVolume;
CREATE PROCEDURE AddVolume(volume_barcode INT, i INT)
  BEGIN
    SELECT @book_id := book_id
    FROM books
    WHERE isbn = i;
    INSERT INTO volumes (barcode, book_id, acquired) VALUES (volume_barcode, @book_id, curdate());
    COMMIT;
  END;

# CALL AddVolume(32, 1);



# MOST POPULAR
# DROP PROCEDURE IF EXISTS PopularBook;
# CREATE PROCEDURE PopularBook(a1 VARCHAR(50), a2 VARCHAR(50), g VARCHAR(20), d DATE) # <- POPR.
#   # authors name, surname , genre, date
#   BEGIN
#     # to get ID
#     SELECT @genre_id := genre_id
#     FROM genres
#     WHERE genre LIKE g;
#
#     SELECT @author_id := author_id
#     FROM authors
#     WHERE (first_name LIKE a1 OR first_name LIKE a2)
#           OR (last_name LIKE a1 OR last_name LIKE a2);
#
#     SELECT
#       title,
#       COUNT(volume_id) loaned
#     FROM books
#       JOIN volumes USING (book_id)
#       JOIN loans USING (volume_id)
#       #       JOIN authors USING (author_id)
#       JOIN book_genres ON books.book_id = book_genres.book_id
#     WHERE loan_date > d AND author_id = @author_id AND genre_id = @genre_id
#     GROUP BY books.book_id
#     ORDER BY loaned DESC
#     LIMIT 10;
#
#     COMMIT;
#   END;

# CALL PopularBook('Isaac', 'Asimov', 'science fiction', '2000-1-1')
