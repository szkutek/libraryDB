import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango, Gdk


class AddUtilities(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADD NEW ...")
        self.label2 = Gtk.Label(" ")

        self.authorLabel = Gtk.Label("Add author:")
        self.authorName = Gtk.Entry()
        self.authorName.set_text("Name")
        self.authorName.set_max_length(50)
        self.authorSurname = Gtk.Entry()
        self.authorSurname.set_text("Surname")
        self.authorSurname.set_max_length(50)
        self.buttonAuthor = Gtk.Button(label="ADD")

        self.publisherLabel = Gtk.Label("Add publisher:")
        self.publisherName = Gtk.Entry()
        self.publisherName.set_text("Publisher")
        self.publisherName.set_max_length(50)
        self.publisherAddress = Gtk.Entry()
        self.publisherAddress.set_text("Address")
        self.publisherAddress.set_max_length(50)
        self.buttonPublisher = Gtk.Button(label="ADD")

        self.classLabel = Gtk.Label("Add classification:")
        self.className = Gtk.Entry()
        self.className.set_max_length(20)
        self.buttonClass = Gtk.Button(label="ADD")

        self.genreLabel = Gtk.Label("Add genre:")
        self.genreName = Gtk.Entry()
        self.genreName.set_max_length(20)
        self.buttonGenre = Gtk.Button(label="ADD")

        self.labelBox = Gtk.Box()
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, False, 0)

        self.authorBox = Gtk.Box(spacing=10)
        self.add(self.authorBox)
        self.authorBox.pack_start(self.authorLabel, False, False, 0)
        self.authorBox.pack_start(self.authorName, True, True, 0)
        self.authorBox.pack_start(self.authorSurname, True, True, 0)
        self.authorBox.pack_start(self.buttonAuthor, True, False, 0)

        self.publisherBox = Gtk.Box(spacing=10)
        self.add(self.publisherBox)
        self.publisherBox.pack_start(self.publisherLabel, False, False, 0)
        self.publisherBox.pack_start(self.publisherName, True, True, 0)
        self.publisherBox.pack_start(self.publisherAddress, True, True, 0)
        self.publisherBox.pack_start(self.buttonPublisher, True, False, 0)

        self.classBox = Gtk.Box(spacing=10)
        self.add(self.classBox)
        self.classBox.pack_start(self.classLabel, False, False, 0)
        self.classBox.pack_start(self.className, True, True, 0)
        self.classBox.pack_start(self.buttonClass, True, False, 0)

        self.genreBox = Gtk.Box(spacing=10)
        self.add(self.genreBox)
        self.genreBox.pack_start(self.genreLabel, False, False, 0)
        self.genreBox.pack_start(self.genreName, True, True, 0)
        self.genreBox.pack_start(self.buttonGenre, True, False, 0)


class AddBook(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        # self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADD A NEW BOOK")
        self.label2 = Gtk.Label(" ")

        self.bookAuthorLabel = Gtk.Label("Choose author:")
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

        self.bookYearLabel = Gtk.Label("Published:")
        self.bookYear = Gtk.Entry()

        self.bookClassLabel = Gtk.Label("Choose classification:")
        self.bookClass = Gtk.Entry()

        self.bookGenreLabel = Gtk.Label("Choose genres:")
        self.bookGenre = Gtk.Entry()

        self.buttonAddBookLabel = Gtk.Label(" ")
        self.buttonAddBook = Gtk.Button(label="ADD BOOK")

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


class AddVolume(Gtk.Box):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADD VOLUME")
        self.label2 = Gtk.Label(" ")

        self.isbnLabel = Gtk.Label("Enter ISBN:")
        self.isbn = Gtk.Entry()
        self.isbn.set_max_length(13)

        self.volumeBarcodeLabel = Gtk.Label("Volume barcode:")
        self.volumeBarcode = Gtk.Entry()
        self.volumeBarcode.set_max_length(8)

        self.buttonAddVolume = Gtk.Button(label="ADD VOLUME")

        padding = 7
        self.volumeLabelBox = Gtk.VBox(spacing=9)
        self.add(self.volumeLabelBox)
        self.volumeLabelBox.pack_start(self.label, False, False, padding)
        self.volumeLabelBox.pack_start(self.isbnLabel, False, False, padding)
        self.volumeLabelBox.pack_start(self.volumeBarcodeLabel, False, False, padding)

        self.volumeBox = Gtk.VBox(spacing=10)
        self.add(self.volumeBox)
        self.volumeBox.pack_start(self.label2, False, False, padding)
        self.volumeBox.pack_start(self.isbn, False, False, 0)
        self.volumeBox.pack_start(self.volumeBarcode, False, False, 0)
        self.volumeBox.pack_start(self.buttonAddVolume, False, False, 0)


class AddStatus(Gtk.TextView):
    def __init__(self):
        Gtk.TextView.__init__(self)

        self.set_editable(False)
        self.set_cursor_visible(False)

        self.set_justification(Gtk.Justification.LEFT)
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 65535, 65535))


class AddPage(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(5)
        self.set_column_spacing(20)

        self.utilities = AddUtilities()
        self.books = AddBook()
        self.volumes = AddVolume()
        self.status = AddStatus()

        self.attach(self.books, 0, 0, 1, 1)
        self.attach(self.volumes, 0, 1, 1, 1)
        self.attach(self.utilities, 1, 0, 1, 1)
        self.attach(self.status, 1, 1, 1, 1)


class RegisterPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("REGISTER NEW CUSTOMER")
        self.label2 = Gtk.Label(" ")

        self.nameLabel = Gtk.Label("Name:")
        self.name = Gtk.Entry()
        self.name.set_max_length(40)

        self.addressLabel = Gtk.Label("Address:")
        self.address = Gtk.Entry()
        self.address.set_max_length(100)

        self.birthDateLabel = Gtk.Label("Birth date:")
        self.birthDate = Gtk.Entry()

        self.phoneNoLabel = Gtk.Label("Phone number:")
        self.phoneNo = Gtk.Entry()
        self.phoneNo.set_max_length(11)

        self.emailLabel = Gtk.Label("Email address:")
        self.email = Gtk.Entry()
        self.email.set_max_length(40)

        self.buttonLabel = Gtk.Label(" ")
        self.button = Gtk.Button(label="REGISTER")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        # self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.nameLabel, False, True, padding)
        self.labelBox.pack_start(self.addressLabel, False, True, padding)
        self.labelBox.pack_start(self.birthDateLabel, False, True, padding)
        self.labelBox.pack_start(self.phoneNoLabel, False, True, padding)
        self.labelBox.pack_start(self.emailLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.name, False, False, 0)
        self.valuesBox.pack_start(self.address, False, False, 0)
        self.valuesBox.pack_start(self.birthDate, False, True, 0)
        self.valuesBox.pack_start(self.phoneNo, False, False, 0)
        self.valuesBox.pack_start(self.email, False, False, 0)
        self.valuesBox.pack_start(self.button, False, False, 0)

        self.statusBox = Gtk.VBox(spacing=10)
        self.add(self.statusBox)

        self.status = Gtk.TextView()
        self.statusBox.pack_start(self.status, True, True, 10)

        self.status.set_editable(False)
        self.status.set_cursor_visible(False)
        self.status.set_justification(Gtk.Justification.LEFT)
        self.status.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 65535, 65535))


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Library")
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.addPage = AddPage()

        self.addUtiPage = Gtk.Box()
        self.addUtiPage.set_border_width(10)
        self.addUtiPage.add(self.addPage)
        self.notebook.append_page(self.addUtiPage, Gtk.Label("Add"))

        self.regPage = RegisterPage()

        self.registerPage = Gtk.Box()
        self.registerPage.set_border_width(10)
        self.registerPage.add(self.regPage)
        self.notebook.append_page(self.registerPage, Gtk.Label('Register'))

        self.deletePage = Gtk.Box()
        self.deletePage.set_border_width(10)
        self.deletePage.add(Gtk.Label('Delete sth:'))
        self.notebook.append_page(self.deletePage, Gtk.Label('Delete'))

        self.updatePage = Gtk.Box()
        self.updatePage.set_border_width(10)
        self.updatePage.add(Gtk.Label('Update sth:'))
        self.notebook.append_page(self.updatePage, Gtk.Label('Update'))

        self.searchPage = Gtk.Box()
        self.searchPage.set_border_width(10)
        self.searchPage.add(Gtk.Label('Search'))
        self.notebook.append_page(self.searchPage, Gtk.Label('Search'))


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
