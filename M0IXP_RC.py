#  Copyright (c) 2020, 2020. David A Hall
#  HumanPenguin@GMail.com
#  All Rights Reserved See Licence.txt for details
#
#

from tabdialog.config import ConfigWindow
import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('handroll', localedir, fallback=True)
_ = translate.gettext


def main():
    new_window = ConfigWindow()
    print(new_window.diag_data)


if __name__ == "__main__":
    main()
