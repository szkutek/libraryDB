DROP PROCEDURE IF EXISTS RentBook;
CREATE PROCEDURE RentBook(cust_barc INT(8), vol_barc INT(8))
  BEGIN
    # potrzebujemy id
    SET @customer_id := (SELECT customer_id
                         FROM customers
                         WHERE customer_barcode = cust_barc);
    # pobieramy id
    SET @volume_id := (SELECT volumes.volume_id
                       FROM volumes
                         JOIN available_volumes USING (volume_id)
                       WHERE barcode = vol_barc);
    # wypożyczamy
    INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
    VALUES (@customer_id, @volume_id, curdate(), ADDDATE(curdate(), 30), NULL);
    COMMIT;
  END;


DROP PROCEDURE IF EXISTS ReturnBook;
CREATE PROCEDURE ReturnBook(vol_barc INT(8))
  BEGIN
    # pobieramy id
    SET @volume_id := (SELECT volume_id
                       FROM volumes
                       WHERE barcode = vol_barc);
    # zwracamy książkę
    UPDATE loans
    SET return_date = curdate()
    WHERE volume_id = @volume_id;
    COMMIT;
  END;


DROP PROCEDURE IF EXISTS AddBook;
CREATE PROCEDURE AddBook(a1 VARCHAR(50), a2 VARCHAR(50), t VARCHAR(100), t_o VARCHAR(100), l VARCHAR(20),
                         i  INT, p_y INT, p VARCHAR(50), c VARCHAR(20))
  BEGIN
    SET @a_id := (SELECT author_id
                  FROM authors
                  WHERE first_name LIKE a1 AND last_name LIKE a2);
    SET @p_id := (SELECT publisher_id
                  FROM publishers
                  WHERE publisher LIKE p);
    SET @c_id := (SELECT classification_id
                  FROM classifications
                  WHERE description LIKE c);
    INSERT INTO books
    (author_id, title, title_original, LANGUAGE, isbn, publish_year, publisher_id, classification_id)
    VALUES (@a_id, t, t_o, l, i, p_y, @p_id, @c_id);
    COMMIT;
  END;


DROP PROCEDURE IF EXISTS AddGenreToBook;
CREATE PROCEDURE AddGenreToBook(i INT, g VARCHAR(20))
  BEGIN
    # potrzebujemy id
    SET @g_id := (SELECT genre_id
                  FROM genres
                  WHERE genre LIKE g);
    # search for book_id
    SET @b_id := (SELECT book_id
                  FROM books
                  WHERE isbn = i);
    # dodajemy do book_genres
    INSERT INTO book_genres
    (book_id, genre_id)
    VALUES (@b_id, @g_id);
    COMMIT;
  END;


DROP PROCEDURE IF EXISTS AddVolume;
CREATE PROCEDURE AddVolume(volume_barcode INT, i INT)
  BEGIN
    SELECT @book_id := book_id
    FROM books
    WHERE isbn = i;
    INSERT INTO volumes (barcode, book_id, acquired) VALUES (volume_barcode, @book_id, curdate());
    COMMIT;
  END;

