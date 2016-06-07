import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Status import Status
from AddVolume import AddVolume
from AddBook import AddBook
from AddUtilities import AddUtilities


class AddPage(Gtk.Grid):
    def __init__(self, lib):
        self.library = lib

        Gtk.Grid.__init__(self)
        self.set_row_spacing(5)
        self.set_column_spacing(20)

        self.utilities = AddUtilities(self.library)
        self.books = AddBook(self.library)
        self.volumes = AddVolume(self.library)
        self.status = Status()

        self.attach(self.books, 0, 0, 1, 1)
        self.attach(self.volumes, 0, 1, 1, 1)
        self.attach(self.utilities, 1, 0, 1, 1)
        self.attach(self.status, 1, 1, 1, 1)
