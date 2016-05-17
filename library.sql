DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

DROP TABLE IF EXISTS book, author, book_author, publisher, classification, genre,
                     book_genre, customer, loan;
# classification and genre(subject) could be an ENUM

CREATE TABLE book (
  book_id INT NOT NULL,
  title VARCHAR(100) NOT NULL ,
  title_original  VARCHAR(100),
  language VARCHAR(20) NOT NULL ,
  isbn  VARCHAR(13),
  edition INT(3),
  publish_year INT(4) NOT NULL ,
  publisher_id  INT NOT NULL ,
  classification_id INT NOT NULL ,
  status ENUM('available','checked out','ordered','lost')
#   barcode ?
);
CREATE TABLE author (
  author_id INT NOT NULL ,
  name VARCHAR(50)  NOT NULL
);
CREATE TABLE book_author (
#   book_author_id  INT NOT NULL , ????
  book_id INT NOT NULL ,
  author_id INT NOT NULL
);
CREATE TABLE publisher (
  publisher_id  INT NOT NULL ,
  name VARCHAR(50) NOT NULL ,
  address VARCHAR(50)
);
CREATE TABLE classification ( # Dewey_Decimal_Classification OR Library_of_Congress_Classification
  classification_id INT NOT NULL ,
  description VARCHAR(20) NOT NULL
);
CREATE TABLE genre (
  genre_id  INT NOT NULL ,
  genre VARCHAR(20) NOT NULL # NOT SURE ABOUT GENRE AND CLASSIFICATION
);
CREATE TABLE book_genre (
#   book_genre_id  INT NOT NULL , ????
  book_id INT NOT NULL ,
  genre_id INT NOT NULL
);
CREATE TABLE customer (
  customer_id INT NOT NULL ,
  name  VARCHAR(40) NOT NULL ,
  birthdate DATE  NOT NULL ,
  address VARCHAR(100)  NOT NULL ,
  phone_no  VARCHAR(11) NOT NULL ,
  email VARCHAR(40) NOT NULL ,
  registration_date DATE  NOT NULL
);
CREATE TABLE loan (
  loan_id INT NOT NULL ,
  customer_id INT NOT NULL ,
  book_id INT NOT NULL ,
  loan_date DATE  NOT NULL ,
  due_date  DATE  NOT NULL ,
  return_date DATE
);