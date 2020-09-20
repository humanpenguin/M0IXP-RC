import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog


def main():
    diag = ConfigDialog()


class Config:
    """ System configuration class. Attempts to read config file. Creates if it dose not exist.

        receives optional config file location and name. Loads file or default if none supplies.
        Launches GUI configuration script if no file found.
    """

    def __init__(self, config_file=None):
        """ Constructor checks for and launches config file creation."""
        self.config_title = " "  # Initial setting of text used all set to empty
        self.config_colour_text = " "
        self.config_file_text = " "
        self.config_font_text = " "
        self.default_bg_colour_text = " "
        self.default_fg_colour_text = " "

        self.default_fg = None
        self.default_bg = None

        self.load_text()  # Load i18n text when done
        self.load_colours()  # Load colours from config file etc.

    def load_text(self):
        """ Set to default for most text will add i18n later. """
        self.config_title = " " + "M0IXP Rotator Control Configuration Window"
        self.config_colour_text = "Colour Selection"
        self.config_file_text = "Configuration File"
        self.config_font_text = "Font Settings"
        self.default_bg_colour_text = "Default Background Colour"
        self.default_fg_colour_text = "Default Foreground Colour"

    def load_colours(self):
        self.default_fg = 'black'
        self.default_bg = 'white'


class ConfigDialog:
    def __init__(self, config=Config(), config_file=None):
        """

        :rtype: object
        """
        self.config = config
        self.diag = ConfigDialog.DialogWindow(config)

    class DialogWindow:
        def __init__(self, config):
            self.config = config
            self.win = dict()  # default top window
            self.create_window()

        def create_window(self):
            win = self.win

            win['top'] = tk.Tk(className=self.config.config_title)
            win['top'].title = self.config.config_title
            win['top'].geometry("900x400")
            win['tabFrame'] = ttk.Notebook(win['top'])
            win['tabFrame'].pack(fill=tk.BOTH)
            win['colourFrame'] = tk.Frame(win['tabFrame'])
            win['fileFrame'] = tk.Frame(win['tabFrame'])
            win['fontFrame'] = tk.Frame(win['tabFrame'])
            win['tabFrame'].add(win['colourFrame'], text=self.config.config_colour_text)

            win['colourLabel'] = tk.Label(win['colourFrame'], text=self.config.config_colour_text)
            #win['colourLabel'].pack()

            #win['default_bg_text'] = ttk.Label(win['colourLabel'], text=self.config.default_bg_colour_text)
            #win['default_bg_choose'] = tk.Button(win['colourLabel'],
            #                                     text="",
            #                                     bg=self.config.default_bg,
            #                                     fg=self.config.default_fg,
            #                                     command="choose_bg_colour")
            #win['default_bg_text'].pack()
            #win['default_bg_choose'].pack()

            #win['default_fg_text'] = ttk.Label(win['colourLabel'], text=self.config.default_fg_colour_text)
            #win['default_fg_choose'] = tk.Button(win['colourLabel'],
            #                                     text="",
            #                                     bg=self.config.default_fg,
            #                                     fg=self.config.default_bg,
            #                                     command="choose_fg_colour")
            #win['default_fg_text'].pack()
            #win['default_fg_choose'].pack()


            win['tabFrame'].add(win['fileFrame'], text=self.config.config_file_text)
            #win['fileFrame'].pack()
            win['tabFrame'].add(win['fontFrame'], text=self.config.config_font_text)

            win['top'].mainloop()

        def choose_bg_colour(self):
            self.config.selected_colour = self.config.default_bg
            self.choose_colour()
            self.config.default_bg = self.config.selected_colour

        def choose_fg_colour(self):
            self.config.selected_colour = self.config.default_fg
            self.choose_colour()
            self.config.default_fg = self.config.selected_colour

        def choose_colour(self):
            self.config.selected_colour = colorchooser.askcolor(color=self.config.selected_colour)


class ConfigBuildFile:
    def __init__(self, config_file=None):
        pass


if __name__ == "__main__":
    main()
