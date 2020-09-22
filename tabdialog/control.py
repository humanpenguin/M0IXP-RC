#  Copyright (c) 2020, 2020. David A Hall
#  HumanPenguin@GMail.com
#  All Rights Reserved See Licence.txt for details
#
#

import serial

class Control:
    def __init__(self):
        pass

    def go_to(self, degree):
        pass


class Gs232Commands:
""" Basic commands to control GS242 rotators this class just contains the basic functions to be written to
    the active serial port.
"""

    def __init__(self, config):
        self.port = config.port

    def right(self):
        self.port.writeln("R")

    def left(self):
        self.port.writeln("L")

    def up(self):
        self.port.writeln("U")

    def down(self):
        self.port.writeln("D")

    def stop_all(self):
        self.port.writeln("S")

    def stop_az(self):
        self.port.writeln("A")

    def stop_el(self):
        self.port.writeln("E")

    def config_az_end(self):
        self.port.writeln("FAE")

    def config_az_start(self):
        self.port.writeln("FAS")

    def config_el_end(self):
        self.port.writeln("FEE")

    def config_el_start(self):
        self.port.writeln("FES")
