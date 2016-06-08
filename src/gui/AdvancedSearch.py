import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AdvancedSearch(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)

        self.library = lib

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADVANCED SEARCH")
        self.label2 = Gtk.Label(" ")

        self.titleLabel = Gtk.Label("Title:")
        self.title = Gtk.Entry()
        self.title.set_max_length(100)

        self.authorLabel = Gtk.Label("Author:")
        self.authorName = Gtk.Entry()
        self.authorSurname = Gtk.Entry()

        self.isbnLabel = Gtk.Label("ISBN:")
        self.isbn = Gtk.Entry()
        self.isbn.set_max_length(13)

        self.publisherLabel = Gtk.Label("Publisher:")
        self.publisher = Gtk.Entry()

        self.classificationLabel = Gtk.Label("Classification:")
        self.classification = Gtk.Entry()  # combo

        self.genreLabel = Gtk.Label("Genres:")
        self.genre = Gtk.Entry()  # combo

        self.languageLabel = Gtk.Label("Language:")
        self.language = Gtk.Entry()  # COMBO BOX

        self.publishYearLabel = Gtk.Label("Publish year:")
        self.publishYear = Gtk.Entry()

        self.buttonSearchLabel = Gtk.Label(" ")
        self.buttonSearch = Gtk.Button(label="SEARCH")
        self.buttonSearch.connect("clicked", self.search)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.authorLabel, False, True, padding)
        self.labelBox.pack_start(self.titleLabel, False, True, padding)
        self.labelBox.pack_start(self.isbnLabel, False, True, padding)
        self.labelBox.pack_start(self.publisherLabel, False, True, padding)
        self.labelBox.pack_start(self.classificationLabel, False, True, padding)
        self.labelBox.pack_start(self.genreLabel, False, True, padding)
        self.labelBox.pack_start(self.languageLabel, False, True, padding)
        self.labelBox.pack_start(self.publishYearLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonSearchLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)

        self.authorBox = Gtk.Box(spacing=5)
        self.valuesBox.add(self.authorBox)
        self.authorBox.pack_start(self.authorName, False, False, 0)
        self.authorBox.pack_start(self.authorSurname, False, False, 0)
        
        self.valuesBox.pack_start(self.title, False, False, 0)
        self.valuesBox.pack_start(self.isbn, False, False, 0)
        self.valuesBox.pack_start(self.publisher, False, False, 0)
        self.valuesBox.pack_start(self.classification, False, False, 0)
        self.valuesBox.pack_start(self.genre, False, False, 0)
        self.valuesBox.pack_start(self.language, False, False, 0)
        self.valuesBox.pack_start(self.publishYear, False, False, 0)
        self.valuesBox.pack_start(self.buttonSearch, False, False, 0)

    def search(self, button):
        authorName = str(self.authorName.get_text())
        authorSurname = str(self.authorSurname.get_text())
        title = str(self.title.get_text())
        isbn = int(self.isbn.get_text())
        publisher = str(self.publisher.get_text())
        classification = str(self.classification.get_text())
        genre = str(self.genre.get_text())
        language = str(self.language.get_text())
        publishYear = int(self.publishYear.get_text())

        results = self.library.query.advanced(parameters=(authorName, authorSurname, title, publishYear,
                                                          publisher, isbn, classification, genre, language))
