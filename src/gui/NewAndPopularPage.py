import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from NewBooks import NewBooks
from PopularBooks import PopularBooks
from Status import Status


class NewAndPopularPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.set_homogeneous(True)

        self.newBooks = NewBooks()
        self.popularBooks = PopularBooks()
        self.status = Status()

        self.newAndPopBox = Gtk.VBox()
        self.add(self.newAndPopBox)
        self.newAndPopBox.add(self.newBooks)
        self.newAndPopBox.add(self.popularBooks)

        self.add(self.status)

