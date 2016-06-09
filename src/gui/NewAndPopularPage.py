import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from NewBooks import NewBooks
from PopularBooks import PopularBooks
from Status import Status


class NewAndPopularPage(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)

        self.library = lib
        self.status = Status()

        self.set_spacing(10)
        self.set_border_width(10)

        self.set_homogeneous(True)

        self.newBooks = NewBooks(self.library, self.status)
        self.popularBooks = PopularBooks(self.library, self.status)

        self.newAndPopBox = Gtk.VBox()
        self.add(self.newAndPopBox)
        self.newAndPopBox.add(self.newBooks)
        self.newAndPopBox.add(self.popularBooks)

        self.add(self.status)
