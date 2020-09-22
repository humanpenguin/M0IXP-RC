#  Copyright (c) 2020, 2020. David A Hall
#  HumanPenguin@GMail.com
#  All Rights Reserved See Licence.txt for details
#

from tabdialog.tabdialog import TabbedDialog
import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('handroll', localedir, fallback=True)
_ = translate.gettext

class ConfigWindow:
    def __init__(self):
        self.diag_data = list()
        self.value_data = list()
        self.load_config()
        self.tab_win = TabbedDialog(title=_("Configuration Setup"),
                                    diag_data=self.diag_data,
                                    values_data=self.value_data)

    def load_config(self):
        """ Handle load files etc later. Create default for now
        """
        dialog_data = [
            {'Type': 'Tab', 'VarName': 'ConfigFile',
             'Max': None, 'Min': None, 'Options': None,
             'Note': 'Configuration File Setup Dialog Window.'},
            {'Type': 'Text', 'VarName': 'ConfigFileName',
             'Max': None, 'Min': None, 'Options': None,
             'Note': _('Configuration File Name.')}
        ]
        dialog_values = [
            {'VarName': 'ConfigFile',
             'Text': _('Configuration File'),
             'Value': _('Config File')},
            {'VarName': 'ConfigFileName',
             'Text': _('Configuration Filename'),
             'Value': '~/m0ixp.cnf'}
        ]
        self.diag_data = dialog_data
        self.value_data = dialog_values
        return
