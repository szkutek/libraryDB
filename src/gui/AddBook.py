import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AddBook(Gtk.Box):
    def __init__(self, lib, stat):
        Gtk.Box.__init__(self)
        # self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(10)
        self.set_border_width(10)

        self.library = lib
        self.status = stat

        self.label = Gtk.Label("ADD A NEW BOOK")
        self.label2 = Gtk.Label(" ")

        self.bookAuthorLabel = Gtk.Label("Author:")
        self.bookAuthor = Gtk.Entry()  # CHANGE TO COMBO BOX

        self.bookTitleLabel = Gtk.Label("Title:")
        self.bookTitle = Gtk.Entry()
        self.bookTitle.set_max_length(100)

        self.bookOrigTitleLabel = Gtk.Label("Original title:")
        self.bookOrigTitle = Gtk.Entry()
        self.bookOrigTitle.set_max_length(100)

        self.bookLanguageLabel = Gtk.Label("Language:")
        self.bookLanguage = Gtk.Entry()  # COMBO BOX

        self.bookIsbnLabel = Gtk.Label("ISBN:")
        self.bookIsbn = Gtk.Entry()
        self.bookIsbn.set_max_length(13)

        self.bookPublisherLabel = Gtk.Label("Publisher:")
        self.bookPublisher = Gtk.Entry()  # COMBO BOX

        self.bookYearLabel = Gtk.Label("Publish year:")
        self.bookYear = Gtk.Entry()

        self.bookClassLabel = Gtk.Label("Choose classification:")
        self.bookClass = Gtk.Entry()

        self.bookGenreLabel = Gtk.Label("Choose genres:")
        self.bookGenre = Gtk.Entry()

        self.buttonAddBookLabel = Gtk.Label(" ")
        self.buttonAddBook = Gtk.Button(label="ADD BOOK")
        self.buttonAddBook.connect("clicked", self.addBook)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.bookAuthorLabel, False, True, padding)
        self.labelBox.pack_start(self.bookTitleLabel, False, True, padding)
        self.labelBox.pack_start(self.bookOrigTitleLabel, False, True, padding)
        self.labelBox.pack_start(self.bookLanguageLabel, False, True, padding)
        self.labelBox.pack_start(self.bookIsbnLabel, False, True, padding)
        self.labelBox.pack_start(self.bookPublisherLabel, False, True, padding)
        self.labelBox.pack_start(self.bookYearLabel, False, True, padding)
        self.labelBox.pack_start(self.bookClassLabel, False, True, padding)
        self.labelBox.pack_start(self.bookGenreLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonAddBookLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.bookAuthor, False, False, 0)
        self.valuesBox.pack_start(self.bookTitle, False, False, 0)
        self.valuesBox.pack_start(self.bookOrigTitle, False, False, 0)
        self.valuesBox.pack_start(self.bookLanguage, False, False, 0)
        self.valuesBox.pack_start(self.bookIsbn, False, False, 0)
        self.valuesBox.pack_start(self.bookPublisher, False, False, 0)
        self.valuesBox.pack_start(self.bookYear, False, False, 0)
        self.valuesBox.pack_start(self.bookClass, False, False, 0)
        self.valuesBox.pack_start(self.bookGenre, False, False, 0)
        self.valuesBox.pack_start(self.buttonAddBook, False, False, 0)

    def addBook(self, button):
        # author, title, original title, language, isbn, publisher,
        # year, classification, genres
        authors = str(self.bookAuthor.get_text())
        author = authors.split(',')
        title = str(self.bookTitle.get_text())
        orig_title = str(self.bookOrigTitle.get_text())
        language = str(self.bookLanguage.get_text())
        isbn = int(self.bookIsbn.get_text())
        publisher = str(self.bookPublisher.get_text())
        year = int(self.bookYear.get_text())
        classification = str(self.bookClass.get_text())
        genre = str(self.bookGenre.get_text())
        genres = genre.split(',')
        self.library.add.book(parameters=(author[0], author[1], title, orig_title, language, isbn,
                                          year, publisher, classification))
        for i in genres:
            self.library.add.genreToBook(parameters=(isbn, i))

        self.status.append(
            'Added new book:\n' +
            '(author, title, original title, language, isbn, publisher, year, classification) \n')
        self.status.append(author[0] + ' ' + author[1]
                           + '; ' + title + '; ' + orig_title + '; ' + language + '; ' + str(isbn) + '; '
                           + publisher + '; ' + str(year) + '; ' + classification + '\n')
        self.status.append('With genres: ' + genre + '\n')
