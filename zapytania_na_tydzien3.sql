# 1. Wyszukiwanie proste dla podanej frazy, np 'asimov'.
# W pythonie pętla bedzie przechodziła po każdym słowie z zapytania i wypluwała wszystkie pasujące wyniki.

SET @zapytanie = 'asimov';

SELECT CONCAT_WS(', ',last_name,first_name) AS author, title, title_original, language, publish_year,
  publisher, isbn
FROM typical_search_query
WHERE last_name REGEXP @zapytanie OR first_name REGEXP @zapytanie OR title REGEXP @zapytanie
    OR title_original REGEXP @zapytanie;

# 2. Wyszukiwanie zaawansowane (w pythonie będzie można wpisać więcej niż 1 słowo do danego pola,
# wtedy procedura będzie taka jak w przypadku wyszukiwanie prostego, oraz będzie można pominąć niektóre pola
# nic do nich nie wpisując).

SET @author='isaac',@title='found',@publish_year=1970,@publisher='s',@isbn='12345';

SELECT CONCAT_WS(', ',last_name,first_name) AS author, title, title_original, language, publish_year,
  publisher, isbn
FROM typical_search_query
WHERE (last_name REGEXP @author OR first_name REGEXP @author)
    AND (title REGEXP @title OR title_original REGEXP @title)
    AND publish_year = @publish_year
    AND publisher REGEXP @publisher
    AND isbn = @isbn;


# 3. Dodawanie książki do biblioteki. Najpierw bibliotekarz będzie musiał dodać odpowiednie gatunki, autora
#  oraz wydawcę, o ile jeszcze nie ma ich w bazie. Następnie wypełnia wymaganie pola:
# title, (opcjonalnie title_original), language, isbn, (edition), publish_year,
# a pozostałe wybiera z listy rozwijanej. Dodatkowo na koniec zaznacza w checkbox odpowiednie genres.
# Poniżej będzie znajdować się pole, dzięki któremu będzie można dodać egzemplarze dla danego numeru isbn.

# Przykładowe inserty jeszcze z punktu pliku sql znajdują się na końcu 'library.sql'.

# W podobny sposób dodajemy nowego czytelnika.


# 4. Wypożyczanie książek. Czytelnikowi o podanym kodzie kreskowym (id) wypożyczamy książkę o danym kodzie. Np.
SELECT * FROM available_volumes; # patrzymy, które książki są dostępne
SET @customer_barcode = 1, @volume_barcode = 2; # podajemy kod kreskowy
SELECT @customer_id:=customer_id FROM customers WHERE customer_barcode = @customer_barcode; # potrzebujemy id
SELECT @volume_id:=volume_id FROM volumes WHERE barcode = @volume_barcode; # pobieramy id

INSERT INTO loans (customer_id, volume_id, loan_date, due_date, return_date)
  VALUES (@customer_id,@volume_id, curdate(), ADDDATE(curdate(),30), NULL); # wypożyczamy

# Natomiast przy oddawaniu książki będzie następujący update:
SET @returned_volume_barcode = 9; # podajemy kod kreskowy
SELECT @volume_id:=volume_id FROM volumes WHERE barcode = @returned_volume_barcode; # pobieramy id
UPDATE loans
  SET return_date = curdate()
  WHERE volume_id = @volume_id; # zwracamy książkę

SELECT * FROM loans;

