DROP PROCEDURE IF EXISTS NewBooks;
CREATE PROCEDURE NewBooks(g VARCHAR(20), l VARCHAR(20), p INT(4), a INT(4))
  BEGIN
    #     SET @genre = g, @lang = l, @publish_year = p, @added_year = a;
    SELECT
      CONCAT_WS(', ', last_name, first_name) author,
      title,
      publish_year,
      genres_concatenated
    FROM books
      JOIN authors USING (author_id)
      JOIN volumes USING (book_id)
      JOIN (SELECT
              book_id,
              GROUP_CONCAT(DISTINCT genre ORDER BY genre ASC SEPARATOR ', ') genres_concatenated
            FROM book_genres
              JOIN genres USING (genre_id)
            GROUP BY book_id) genresConc
        ON books.book_id = genresConc.book_id
      JOIN book_genres ON books.book_id = book_genres.book_id
      JOIN genres USING (genre_id)
    WHERE genre = g
          AND language = l
          AND YEAR(acquired) = a
          AND publish_year = p;
  END;


DROP PROCEDURE IF EXISTS PopularBooks;
CREATE PROCEDURE PopularBooks(a_name VARCHAR(50), a_surname VARCHAR(50), g VARCHAR(20), d DATE)
  BEGIN
    SET @author_name = a_name, @author_surname = a_surname, @genre = g, @since = d;
    SELECT
      CONCAT_WS(', ', last_name, first_name) author,
      title,
      COUNT(volume_id)                       x_times_loaned
    FROM books
      JOIN volumes USING (book_id)
      JOIN loans USING (volume_id)
      JOIN authors USING (author_id)
      JOIN book_genres ON books.book_id = book_genres.book_id
      JOIN genres USING (genre_id)
    WHERE loan_date >= @since
          AND genre LIKE @genre
          AND first_name REGEXP @author_name
          AND last_name REGEXP @author_surname
    GROUP BY books.book_id
    ORDER BY x_times_loaned DESC
    LIMIT 10;

  END;
