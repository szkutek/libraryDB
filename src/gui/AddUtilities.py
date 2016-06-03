import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AddUtilities(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("ADD NEW AUTHOR / PUBLISHER / GENRE / CLASSIFICATION")
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
