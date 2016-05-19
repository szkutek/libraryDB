DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

DROP TABLE IF EXISTS book, author, book_author, publisher, classification, genre,
                     book_genre, customer, loan;

CREATE TABLE book (
  book_id INT NOT NULL AUTO_INCREMENT ,
  title VARCHAR(100) NOT NULL ,
  title_original  VARCHAR(100),
  language VARCHAR(20) NOT NULL ,
  isbn  VARCHAR(13) ,
  edition INT(3) ,
  publish_year INT(4) NOT NULL ,
  publisher_id  INT NOT NULL ,
  classification_id INT NOT NULL ,
  status ENUM('available','checked out','ordered','lost') ,
  PRIMARY KEY (book_id),
  FOREIGN KEY (publisher_id) REFERENCES publisher (publisher_id) ON DELETE CASCADE ,
  FOREIGN KEY (classification_id) REFERENCES classification (classification_id) ON DELETE CASCADE ,
  UNIQUE KEY (isbn)
);

CREATE TABLE author (
  author_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50)  NOT NULL,
  PRIMARY KEY (author_id)
);

CREATE TABLE book_author (
#   book_author_id  INT NOT NULL , ????
  book_id INT NOT NULL ,
  author_id INT NOT NULL ,
  PRIMARY KEY (book_id, author_id) ,
  FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE ,
  FOREIGN KEY (author_id) REFERENCES author (author_id) ON DELETE CASCADE
);

CREATE TABLE publisher (
  publisher_id  INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL ,
  address VARCHAR(50) ,
  PRIMARY KEY (publisher_id) ,
  UNIQUE KEY (name)
);

CREATE TABLE classification ( # Dewey_Decimal_Classification OR Library_of_Congress_Classification
  classification_id INT NOT NULL AUTO_INCREMENT ,
  description VARCHAR(20) NOT NULL ,
  PRIMARY KEY (classification_id) ,
  UNIQUE KEY (description) # <- is it necessary?
);

CREATE TABLE genre (
  genre_id  INT NOT NULL AUTO_INCREMENT,
  genre VARCHAR(20) NOT NULL , # NOT SURE ABOUT GENRE AND CLASSIFICATION
  PRIMARY KEY (genre_id) ,
  UNIQUE KEY (genre)
);

CREATE TABLE book_genre (
#   book_genre_id  INT NOT NULL , ????
  book_id INT NOT NULL ,
  genre_id INT NOT NULL ,
  PRIMARY KEY (book_id, genre_id) ,
  FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE ,
  FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE CASCADE
);

CREATE TABLE customer (
  customer_id INT NOT NULL AUTO_INCREMENT ,
  name  VARCHAR(40) NOT NULL ,
  birthdate DATE  NOT NULL ,
  address VARCHAR(100)  NOT NULL ,
  phone_no  VARCHAR(11),
  email VARCHAR(40),
  registration_date DATE  NOT NULL ,
  PRIMARY KEY (customer_id)
);

CREATE TABLE loans (
  loan_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL ,
  book_id INT NOT NULL ,
  loan_date DATE  NOT NULL ,
  due_date  DATE  NOT NULL ,
  return_date DATE ,
  PRIMARY KEY (loan_id) ,
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE CASCADE ,
  FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE
);