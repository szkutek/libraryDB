DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

DROP TABLE IF EXISTS books, volumes, authors, book_authors, publishers, classifications, genres,
book_genres, customers, loans;


CREATE TABLE customers (
  customer_id       INT          NOT NULL AUTO_INCREMENT,
  customer_barcode  INT          NOT NULL,
  name              VARCHAR(40)  NOT NULL,
  birth_date        DATE         NOT NULL,
  address           VARCHAR(100) NOT NULL,
  phone_no          VARCHAR(11),
  email             VARCHAR(40),
  registration_date DATE         NOT NULL,
  PRIMARY KEY (customer_id),
  UNIQUE KEY (customer_barcode)
);

CREATE TABLE authors (
  author_id  INT         NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name  VARCHAR(50) NOT NULL,
  PRIMARY KEY (author_id)
);

CREATE TABLE publishers (
  publisher_id INT         NOT NULL AUTO_INCREMENT,
  publisher    VARCHAR(50) NOT NULL,
  address      VARCHAR(50),
  PRIMARY KEY (publisher_id),
  UNIQUE KEY (publisher)
);

CREATE TABLE classifications (
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
  author_id         INT          NOT NULL,
  title             VARCHAR(100) NOT NULL,
  title_original    VARCHAR(100),
  language          ENUM ('Polish', 'English', 'German', 'Russian', 'Other'),
  isbn              INT(13),
  publish_year      INT(4)       NOT NULL,
  publisher_id      INT          NOT NULL,
  classification_id INT          NOT NULL,
  PRIMARY KEY (book_id),
  FOREIGN KEY (author_id) REFERENCES authors (author_id),
  FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id),
  FOREIGN KEY (classification_id) REFERENCES classifications (classification_id),
  UNIQUE KEY (isbn)
);

CREATE TABLE volumes (
  volume_id INT NOT NULL AUTO_INCREMENT,
  barcode   INT NOT NULL,
  book_id   INT NOT NULL,
  acquired  DATE,
  PRIMARY KEY (volume_id),
  FOREIGN KEY (book_id) REFERENCES books (book_id)
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


CREATE OR REPLACE VIEW available_volumes AS
  SELECT
    book_id,
    volume_id
  FROM volumes
  WHERE
    volume_id NOT IN (SELECT volume_id
                      FROM loans)
    OR volume_id IN (SELECT volume_id AS ID_available
                     FROM loans
                     WHERE return_date IS NOT NULL)
  ORDER BY book_id;


INSERT INTO classifications (description) VALUES ('fiction');
INSERT INTO genres (genre) VALUES ('fantasy'), ('science fiction'), ('detective novel');
INSERT INTO authors (first_name, last_name) VALUES ('Isaac', 'Asimov'), ('Arthur Conan', 'Doyle');
INSERT INTO publishers (publisher, address) VALUES ('Something', 'New York, USA');
INSERT INTO customers (customer_barcode, name, birth_date, address, phone_no, email, registration_date)
VALUES ('1', 'Agnieszka Szkutek', '1994-08-04', 'bla, bla', '1234', 'email', curdate());
INSERT INTO books (author_id, title, title_original, language, isbn, publish_year, publisher_id, classification_id)
VALUES ('1', 'Robots', '', 'English', '1234', '1951', '1', '1'),
  ('1', 'Foundation', '', 'English', '12345', '1970', '1', '1'),
  ('2', 'A Study in Scarlet', '', 'English', '123', '1970', '1', '1');
INSERT INTO book_genres (book_id, genre_id) VALUES ('1', '1'), ('1', '2'), ('2', '2'), ('3', '3');
INSERT INTO volumes (barcode, book_id, acquired) VALUES
  (1, '1', '1960-1-1'), (2, '1', '2000-1-1'), (3, '1', '1990-1-1'),
  (4, '2', '1960-1-1'), (5, '2', '2000-1-1'), (6, '2', '1990-1-1'),
  (7, '2', '1960-1-1'), (8, '3', '2000-1-1'), (9, '3', '1990-1-1');
INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
VALUES ('1', '1', curdate(), ADDDATE(curdate(), 31), NULL),
  ('1', '3', '2016-3-4', ADDDATE('2016-3-4', 30), '2016-4-30'),
  ('1', '9', '2016-4-4', ADDDATE('2016-4-4', 30), NULL);

SELECT * FROM customers;

SELECT * FROM loans;