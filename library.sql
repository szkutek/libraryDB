DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

DROP TABLE IF EXISTS books, volumes, authors, book_authors, publishers, classifications, genres,
book_genres, customers, loans;


CREATE TABLE customers (
  customer_id       INT          NOT NULL AUTO_INCREMENT,
  customer_barcode  INT          NOT NULL,
  name              VARCHAR(40)  NOT NULL,
  birthdate         DATE         NOT NULL,
  address           VARCHAR(100) NOT NULL,
  phone_no          VARCHAR(11),
  email             VARCHAR(40),
  registration_date DATE         NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE authors (
  author_id INT         NOT NULL AUTO_INCREMENT,
  first_name      VARCHAR(50) NOT NULL,
  last_name      VARCHAR(50) NOT NULL,
  PRIMARY KEY (author_id)
);

CREATE TABLE publishers (
  publisher_id INT         NOT NULL AUTO_INCREMENT,
  name         VARCHAR(50) NOT NULL,
  address      VARCHAR(50),
  PRIMARY KEY (publisher_id),
  UNIQUE KEY (name)
);

CREATE TABLE classifications (# Dewey_Decimal_Classification OR Library_of_Congress_Classification
  classification_id INT         NOT NULL AUTO_INCREMENT,
  description       VARCHAR(20) NOT NULL,
  PRIMARY KEY (classification_id),
  UNIQUE KEY (description)
);

CREATE TABLE genres (
  genre_id INT         NOT NULL AUTO_INCREMENT,
  genre    VARCHAR(20) NOT NULL,
  PRIMARY KEY (genre_id),
  UNIQUE KEY (genre)
);

CREATE TABLE books (
  book_id           INT          NOT NULL AUTO_INCREMENT,
  title             VARCHAR(100) NOT NULL,
  title_original    VARCHAR(100),
  language          VARCHAR(20)  NOT NULL,
  isbn              VARCHAR(13),
  edition           INT(3),
  publish_year      INT(4)       NOT NULL,
  publisher_id      INT          NOT NULL,
  classification_id INT          NOT NULL,
  PRIMARY KEY (book_id),
  FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id),
  FOREIGN KEY (classification_id) REFERENCES classifications (classification_id),
  UNIQUE KEY (isbn)
);

CREATE TABLE volumes (
  volume_id INT NOT NULL AUTO_INCREMENT,
  barcode   INT NOT NULL,
  book_id   INT NOT NULL,
  aquired   DATE,
  PRIMARY KEY (volume_id),
  FOREIGN KEY (book_id) REFERENCES books (book_id)
    ON DELETE CASCADE
);

CREATE TABLE book_authors (
  book_id   INT NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY (book_id, author_id),
  FOREIGN KEY (book_id) REFERENCES books (book_id)
    ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors (author_id)
    ON DELETE CASCADE
);

CREATE TABLE book_genres (
  book_id  INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (book_id, genre_id),
  FOREIGN KEY (book_id) REFERENCES books (book_id)
    ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
    ON DELETE CASCADE
);

CREATE TABLE loans (
  loan_id     INT  NOT NULL AUTO_INCREMENT,
  customer_id INT  NOT NULL,
  volume_id   INT  NOT NULL,
  loan_date   DATE NOT NULL,
  due_date    DATE NOT NULL,
  return_date DATE,
  PRIMARY KEY (loan_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    ON DELETE CASCADE,
  FOREIGN KEY (volume_id) REFERENCES volumes (volume_id)
    ON DELETE CASCADE
);

CREATE OR REPLACE VIEW book_genres_compilation AS
  SELECT title, GROUP_CONCAT(DISTINCT genre ORDER BY genre ASC SEPARATOR ', ') FROM
    books JOIN book_genres USING (book_id)
  JOIN genres USING (genre_id);

# CREATE OR REPLACE VIEW availability AS
  SELECT book_id,
    CONCAT_WS('/', COUNT(volume_id), (SELECT COUNT(volume_id) FROM volumes GROUP BY book_id)) AS `available/all`
  FROM volumes LEFT JOIN loans USING (volume_id)
  GROUP BY book_id;

CREATE OR REPLACE VIEW availability AS
  SELECT books.book_id,
#     CONCAT_WS('/', COUNT(volume_id),
#               (SELECT COUNT(volume_id) FROM volumes GROUP BY book_id)) AS `available/all`
    COUNT(volume_id) available_volumes,
    (SELECT COUNT(volume_id) FROM volumes GROUP BY book_id) all_volumes
  FROM books LEFT JOIN
      (SELECT book_id, volume_id FROM volumes
        WHERE
          volume_id NOT IN (SELECT volume_id FROM loans)
          OR volume_id IN (SELECT volume_id AS ID_available FROM loans
                           WHERE return_date IS NOT NULL)
      ) availableVolumes
    ON books.book_id = availableVolumes.book_id
  GROUP BY books.book_id;



CREATE OR REPLACE VIEW book_authors_compilation AS
  SELECT CONCAT_WS(', ', last_name, first_name), title
  FROM books JOIN book_authors USING (book_id)
  JOIN authors USING (author_id);


SELECT * FROM books;
DELETE FROM customers;

SELECT
  authors.name AS author, title, language, publish_year, publishers.name AS publisher
FROM books
  JOIN book_authors USING (book_id)
  JOIN authors ON book_authors.author_id = authors.author_id
JOIN publishers ON publishers.publisher_id = books.publisher_id;

INSERT INTO classifications (description) VALUES ('fiction');
INSERT INTO genres (genre) VALUES ('fantasy'), ('science fiction');
INSERT INTO authors (name) VALUES ('Isaac Asimov');
INSERT INTO publishers (name, address) VALUES ('Doubleday', 'NYC');
INSERT INTO customers (customer_barcode, name, birthdate, address, phone_no, email, registration_date)
VALUES ('00000001','Aga Szkutek', '1994-08-04', 'Ligonia, Cieszyn', '500026089', 'aga.szkutek@gmail.com', now());
INSERT INTO books (title, title_original, language, isbn, edition, publish_year, publisher_id, classification_id)
VALUES ('Robots','','english','1234','1','1951','1','1');
INSERT INTO book_genres (book_id, genre_id) VALUES ('2','1'),('2','2');
INSERT INTO book_authors (book_id, author_id) VALUES ('2','1');
INSERT INTO volumes (barcode, book_id, aquired) VALUES ('00000001','2','1960-1-1'),('00000002','2','2000-1-1');
INSERT INTO volumes (barcode, book_id, aquired) VALUES ('00000003','2','1990-1-1');

SELECT * FROM book_genres_compilation;
SELECT * FROM loans;

INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
    VALUES ('1','1', now(), ADDDATE(now(),31), NULL);
INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
    VALUES ('1','3', '2016-3-4', ADDDATE(now(),30), '2016-4-30');


