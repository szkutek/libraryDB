import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Status(Gtk.TextView):
    def __init__(self):
        Gtk.TextView.__init__(self)

        self.set_editable(False)
        self.set_cursor_visible(False)

        self.set_justification(Gtk.Justification.LEFT)
        # self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 65535, 65535))
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(45535, 45535, 45535))
