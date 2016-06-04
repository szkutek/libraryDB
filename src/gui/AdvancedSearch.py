import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AdvancedSearch(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADVANCED SEARCH")
        self.label2 = Gtk.Label(" ")

        self.bookTitleLabel = Gtk.Label("Title:")
        self.bookTitle = Gtk.Entry()
        self.bookTitle.set_max_length(100)

        self.bookAuthorLabel = Gtk.Label("Author:")
        self.bookAuthor = Gtk.Entry()

        self.bookIsbnLabel = Gtk.Label("ISBN:")
        self.bookIsbn = Gtk.Entry()
        self.bookIsbn.set_max_length(13)

        self.bookPublisherLabel = Gtk.Label("Publisher:")
        self.bookPublisher = Gtk.Entry()

        self.bookClassLabel = Gtk.Label("Classification:")
        self.bookClass = Gtk.Entry()  # combo

        self.bookGenreLabel = Gtk.Label("Genres:")
        self.bookGenre = Gtk.Entry()  # combo

        self.bookLanguageLabel = Gtk.Label("Language:")
        self.bookLanguage = Gtk.Entry()  # COMBO BOX

        self.bookYearLabel = Gtk.Label("Publish year:")
        self.bookYear = Gtk.Entry()

        self.buttonSearchLabel = Gtk.Label(" ")
        self.buttonSearch = Gtk.Button(label="SEARCH")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.bookAuthorLabel, False, True, padding)
        self.labelBox.pack_start(self.bookTitleLabel, False, True, padding)
        self.labelBox.pack_start(self.bookIsbnLabel, False, True, padding)
        self.labelBox.pack_start(self.bookPublisherLabel, False, True, padding)
        self.labelBox.pack_start(self.bookClassLabel, False, True, padding)
        self.labelBox.pack_start(self.bookGenreLabel, False, True, padding)
        self.labelBox.pack_start(self.bookLanguageLabel, False, True, padding)
        self.labelBox.pack_start(self.bookYearLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonSearchLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.bookAuthor, False, False, 0)
        self.valuesBox.pack_start(self.bookTitle, False, False, 0)
        self.valuesBox.pack_start(self.bookIsbn, False, False, 0)
        self.valuesBox.pack_start(self.bookPublisher, False, False, 0)
        self.valuesBox.pack_start(self.bookClass, False, False, 0)
        self.valuesBox.pack_start(self.bookGenre, False, False, 0)
        self.valuesBox.pack_start(self.bookLanguage, False, False, 0)
        self.valuesBox.pack_start(self.bookYear, False, False, 0)
        self.valuesBox.pack_start(self.buttonSearch, False, False, 0)
