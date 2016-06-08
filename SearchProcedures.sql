# SIMPLE SEARCH
DROP PROCEDURE IF EXISTS CreateSearchTmp;
CREATE PROCEDURE CreateSearchTmp(IN lang VARCHAR(20), IN year1 INT(4), IN year2 INT(4))
  BEGIN
    DROP TABLE IF EXISTS SearchTmp;
    CREATE TEMPORARY TABLE IF NOT EXISTS SearchTmp (
      search_id      INT          NOT NULL AUTO_INCREMENT,
      first_name     VARCHAR(50)  NOT NULL,
      last_name      VARCHAR(50)  NOT NULL,
      title          VARCHAR(100) NOT NULL,
      title_original VARCHAR(100),
      publish_year   INT(4)       NOT NULL,
      available      INT          NOT NULL,
      PRIMARY KEY (search_id)
    );

    INSERT INTO SearchTmp (first_name, last_name, title, title_original, publish_year, available)
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
    COMMIT;
  END;


DROP PROCEDURE IF EXISTS SimpleSearch;
CREATE PROCEDURE SimpleSearch(w VARCHAR(20))
  BEGIN
    SET @word = w;
    SELECT
      CONCAT_WS(',', last_name, first_name) AS author,
      title,
      publish_year,
      available
    FROM SearchTmp
    WHERE first_name REGEXP @word
          OR last_name REGEXP @word
          OR title REGEXP @word
          OR title_original REGEXP @word;
  END;

# ADVANCED SEARCH
# SET @author = 'isaac', @title = 'found', @publish_year = 1970, @publisher = 's', @isbn = '12345';
DROP PROCEDURE IF EXISTS AdvancedSearch;
CREATE PROCEDURE AdvancedSearch(a1  VARCHAR(50), a2 VARCHAR(50), t VARCHAR(100),
                                p_y INT, p VARCHAR(50), i INT,
                                c   VARCHAR(20), g VARCHAR(20), l VARCHAR(20))
  #   authorName, authorSurname, title, publishYear, publisher, isbn, classification, genre, language
  BEGIN
    SELECT @g_id := genre_id
    FROM genres
    WHERE genre LIKE g;

    SELECT
      CONCAT_WS(', ', last_name, first_name) AS author,
      title,
      publish_year,
      language,
      publisher,
      COUNT(volume_id)                          available
    FROM books
      JOIN (SELECT
              book_id,
              genre_id
            FROM book_genres
            WHERE genre_id = @g_id) genres2
        ON genres2.book_id = books.book_id
      JOIN authors USING (author_id)
      JOIN available_volumes ON books.book_id = available_volumes.book_id
      JOIN publishers USING (publisher_id)
      JOIN classifications USING (classification_id)
    WHERE (last_name REGEXP a1 OR first_name REGEXP a2)
          AND (title REGEXP t OR title_original REGEXP t)
          AND publish_year = p_y
          AND publisher REGEXP p
          AND isbn = i
          AND description LIKE c
          AND language = l;
  END;

# CALL AdvancedSearch('Isaac', 'a', 'o', 1970, 's', 12345, 'fiction', 'science fiction', 'English');