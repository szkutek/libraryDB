# 1.  Wyszukiwanie proste dla podanej frazy, np 'asimov' + pokazanie ilości dostępnych egzemplarzy.
# W pythonie pętla bedzie przechodziła po każdym słowie z zapytania i wypluwała wszystkie pasujące wyniki.
# Dodatkowo będzie można zawęzić poszukiwania wybierając język oraz przedział czasowy, w jakim książka
# została wydana.

SET @zapytanie = 'asimov'; # będzie można wybrać z listy rozwijanej jakiego pola to dotyczy np autor/ tytuł
SET @lang = 'English', @date1 = 1960, @date2 = 1970;

SELECT
  CONCAT_WS(', ', last_name, first_name) AS author,
  title,
  publish_year,
  COUNT(volume_id)                          available
FROM books
  JOIN authors USING (author_id)
  JOIN available_volumes ON books.book_id = available_volumes.book_id
WHERE (last_name REGEXP @zapytanie
       OR first_name REGEXP @zapytanie
       OR title REGEXP @zapytanie
       OR title_original REGEXP @zapytanie)
      AND books.language = @lang
      AND (books.publish_year BETWEEN @date1 AND @date2)
GROUP BY books.book_id;

# 2. Wyszukiwanie zaawansowane (w pythonie będzie można wpisać więcej niż 1 słowo do danego pola,
# wtedy procedura będzie taka jak w przypadku wyszukiwanie prostego + będzie można pominąć niektóre pola
# nic do nich nie wpisując).

SET @author = 'isaac', @title = 'found', @publish_year = 1970, @publisher = 's', @isbn = '12345';

SELECT
  CONCAT_WS(', ', last_name, first_name) AS author,
  title,
  publish_year,
  language,
  publisher,
  COUNT(volume_id)                          available
FROM books
  JOIN authors USING (author_id)
  JOIN available_volumes ON books.book_id = available_volumes.book_id
  JOIN publishers USING (publisher_id)
WHERE (last_name REGEXP @author OR first_name REGEXP @author)
      AND (title REGEXP @title OR title_original REGEXP @title)
      AND publish_year = @publish_year
      AND publisher REGEXP @publisher
      AND isbn = @isbn;

# 3. Wykaz nowości, zawężenie do kilku działów/tematyki, zawężenie do języka,
# można wybrać rok wydania / rok przyjęcia do księgozbioru (do kilku lat wstecz, z listy rozwijanej)
SELECT *
FROM books;
SET @title='f';
SET @genre1 = 'fantasy', @genre2 = 'science fiction', @lang = 'English', @rok_dod = 2000, @rok_wyd = 1970;

SELECT
  authors.last_name,
  title,
  publish_year,
  genre
FROM books
  JOIN authors USING (author_id)
  JOIN volumes USING (book_id)
  JOIN book_genres ON books.book_id = book_genres.book_id
  JOIN genres USING (genre_id)
WHERE (genre = @genre1 OR genre = @genre2)
      AND language = @lang
      AND YEAR(acquired) = @rok_dod
      AND publish_year = @rok_wyd
      AND books.title REGEXP @title;


# 4. Najbardziej popularny tytuł (z uwzględnieniem autora i/lub gatunku)

# tytuł
SELECT
  title,
  COUNT(volume_id) loaned,
  all_volumes
FROM books
  JOIN volumes USING (book_id)
  JOIN loans USING (volume_id)
  JOIN (SELECT
          book_id,
          COUNT(volume_id) all_volumes
        FROM volumes
        GROUP BY book_id) allVols
    ON books.book_id = allVols.book_id
# WHERE loan_date > '2016-5-1'
GROUP BY books.book_id
ORDER BY loaned DESC
LIMIT 10;

# # gatunek
# SELECT
#   genre,
#   COUNT(books.book_id) loaned,
#   all_books
# FROM
#   genres
#   JOIN book_genres USING (genre_id)
#   JOIN books USING (book_id)
#   JOIN (SELECT
#           genre_id,
#           COUNT(book_id) all_books
#         FROM book_genres
#         GROUP BY genre_id) allBooks
#     ON genres.genre_id = allBooks.genre_id
# WHERE book_id IN (SELECT book_id
#                   FROM volumes
#                     JOIN loans USING (volume_id))
# GROUP BY genres.genre_id
# ORDER BY loaned DESC
# LIMIT 10;
#
# SELECT * FROM customers;
# # autor:
# SELECT
#   CONCAT_WS(', ', authors.last_name, authors.first_name) author,
#   COUNT(volume_id)                                       loaned,
#   all_volumes
# FROM authors
#   JOIN books USING (author_id)
#   JOIN (SELECT
#           author_id,
#           COUNT(volume_id) AS all_volumes
#         FROM books
#           LEFT JOIN volumes USING (book_id)
#         GROUP BY author_id) allVolsPerAuthor
#     ON authors.author_id = allVolsPerAuthor.author_id
#   JOIN (SELECT
#           book_id,
#           volume_id
#         FROM loans
#           JOIN volumes USING (volume_id)) loanedVols
#     ON books.book_id = loanedVols.book_id
# GROUP BY authors.author_id
# ORDER BY loaned DESC
# LIMIT 10;