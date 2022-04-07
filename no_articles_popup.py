from os.path import exists

import gi

import regression_calc
import vector_creator
from statics import VERSION_CODE

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class NoArticlesPopup:
    result = ""
    callback = None
    close_callback = None
    title = ""

    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title("Don't Read It {}".format(VERSION_CODE))
        # self.window.resize(500, 250)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        msg = Gtk.Label("You don't have any articles downloaded. Go download some first.\nExplanation is in the Git "
                        "Readme. ")
        button = Gtk.Button("Okay")
        button.connect("button-press-event", self.submit)
        self.window.add(box)
        box.add(msg)
        box.add(button)

    def submit(self, b, c):
        self.window.destroy()
        Gtk.main_quit()

    def show_window(self):
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
        Gtk.main()

    if exists("styles.css"):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("./styles.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
