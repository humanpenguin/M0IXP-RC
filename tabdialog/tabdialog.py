#  Copyright (c) 2020, 2020. David A Hall
#  HumanPenguin@GMail.com
#  All Rights Reserved See Licence.txt for details
#
#

import tkinter as tk
from tkinter import ttk
import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('handroll', localedir, fallback=True)
_ = translate.gettext

#  from tkinter import colorchooser
#  from tkinter import filedialog


class TabbedDialog:
    def __init__(self, title="", diag_data=None, values_data=None) -> object:
        """
        Takes a formatted list of dicts diag_data
         and a dict containing values for defaults or return.

        Tests the format for diag_dict and values dict
        and returns an error if data is missing miss
        formatted.

        diag_data
        Type: List
        Format: [
            {'Type':'',             # Type of element to follow
                                    # So Far : Tab | Text | Integer | List | Real | Colour | Font
                                    # Tab must be the first and every element following
                                    # will be assigned to the same Tab
             'VarName':'',          # Text used to link this value to values_data
                                    # This is a variable name and never displayed. i18n
                                    # is used to generate the actual name string to display
                                    # this string is then stored in values_data
             'Max',,                # Only used for numerical types
             'Min',,                # Only used for numerical types
             'Options',{'Type',[]}, # Only used for list types Type can be Char Int or Text
             'Note',''              # Text must all be values supported by i18n
        }]

        values_data
        Type: list of dict
        Format: [{'VarName','', # Short var name used to link values to definitions
                 'Text','',    # Text used to pull i18n description for display
                 'Value',,     # Check for None default value supplied or value tobe returned
                }]

        As varName is used to link the 2 data structures the fact that they are of equal size
        and each Match must be checked.

        :param diag_data: Ordered List of Dicts
        :param values_data: Dict
        """
        self.diag_data = diag_data
        self.values_data = values_data
        self.title = title
        self.win = Window(self)

    def test_data(self):
        """
        Returns True if no error is found in either supplied data structure

        :return:
        """
        if self.diag_data is None:  # No Data
            return False
        elif self.values_data is None:  # No Data
            return False
        elif len(self.diag_data) != len(self.values_data):  # Unmatched values
            return False
        return True


class Window:
    def __init__(self, parent=None):
        if parent is None:
            self.parent = TabbedDialog()  # should really only happen in testing.
        else:
            self.parent = parent
        self.root = tk.Tk()
        self.root.title = self.parent.title
        self.winElements = dict()
        self.winElements.update({'Notebook': ttk.Notebook(self.root)})
        self.add_elements()
        self.root.mainloop()

    def get_values(self, varname):
        value_tbr = None
        value_data = self.parent.values_data
        for value in value_data:
            if value['VarName'] == varname:
                value_tbr = value
        if value_tbr is None:
            raise Exception("TabbedDialog __Window get_values Exception: Missing value VarName: "
                            + varname)
        return value_tbr

    def add_elements(self):
        # Tab | Text | Integer | List | Real | Colour | Font
        for element in self.parent.diag_data:
            if element['Type'] == 'Tab':
                self.create_tab(element)
            elif element['Type'] == 'Text':
                self.create_text(element)
            elif element['Type'] == 'Integer':
                self.create_integer(element)
            elif element['Type'] == 'List':
                self.create_list(element)
            elif element['Type'] == 'Real':
                self.create_real(element)
            elif element['Type'] == 'Colour':
                self.create_colour(element)
            elif element['Type'] == 'Font':
                self.create_font(element)

    def create_tab(self, element):
        new_frame = tk.Frame(self.root)
        values = self.get_values(element['VarName'])
        text = values['Text']
        self.winElements['Notebook'].add(new_frame, text=text)
        self.winElements.update({element['VarName']: new_frame})

    def create_text(self, element):
        values = self.get_values(element['VarName'])
        text = values['Text']
        new_label = tk.Label(self.root, text=text)
        val = values['Value']
        val_st_var = tk.StringVar()
        val_st_var.set(_(val))
        values['Value'] = val_st_var
        new_text_input = tk.Label(self.root, textvariable=values['Value'])
        self.winElements.update({element['VarName' + 'Label']: new_label})
        self.winElements.update({element['VarName' + 'Input']: new_text_input})

    def create_integer(self, element):
        values = self.get_values(element['VarName'])
        text = _(values['text'])
        new_label = tk.Label(self.root, text=text)
        val = values['Value']
        val_int_var = tk.IntVar()
        val_int_var.set(_(val))
        values['Value'] = val_int_var
        new_int_input = tk.Spinbox(self.root,
                                   textvariable=values['Value'],
                                   from_=values['Min'],
                                   to=values['Max'])
        self.winElements.update({element['VarName' + 'Label']: new_label})
        self.winElements.update({element['VarName' + 'Input']: new_int_input})

    def create_real(self, element):
        pass

    def create_list(self, element):
        pass

    def create_colour(self, element):
        pass

    def create_font(self, element):
        pass
