"""Startet ein volles Schiffeversenken Spiel
"""
import sys
import time

from .master import Master

def main(_argv):
    """Main, die das Modul schiffeversenken ausfuehrt.

    Args:
        _argv ([type]):
    """
    master: Master = Master()
    master.print_willkommensnachricht()
    time.sleep(3)
    master.clear_terminal()
    auswahl: int = master.print_menu()
    master.initialisieren(auswahl)
    while not master.ist_spiel_vorbei:
        master.spielen()


if __name__ == '__main__':
    main(sys.argv)
