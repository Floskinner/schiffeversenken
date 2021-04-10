"""[DocString]
"""
import sys
import os
import platform
import time


class Master:
    """[summary]
    """


    def print_spielfeld(self):
        """
        Gibt Spielfeld aus.
        """
        spielfeld = [[1,1,1,1,1,0,0,0,0,0],[2,2,0,0,0,0,0,0,0,0]]
        print("\u1F7E5")

    def neues_spiel(self):
        """
        Erstellt leeres Spielfeld,
        fragt Spielernamen ab            
        """
        print()
    
    def print_willkommensnachricht(self):
        """
        Gibt Willkommensnachricht aus
        """
        print("\u2554", end='')
        i=0
        while i < 71:
            print("\u2550", end='')
            i=i+1
        print("\u2557", end='')
        print()
        print("\u2551\t  _____              _          _      ___   ___\t\t\u2551")
        print("\u2551\t / ____|            | |        |_|    / __| / __|   ___\\ \t\u2551")
        print("\u2551\t| (___       ____   | |___      _    | |__  | |__  / __ \\\t\u2551")
        print("\u2551\t\\___  \\    /  __|   |     \\    | |   |  __| | ___|| |__|_|\t\u2551")
        print("\u2551\t ____) |  |  (___   |  __  |   | |   | |    | |   | |_____\t\u2551")
        print("\u2551\t|_____/    \\____|   |_|  |_|   |_|   |_|    |_|   \\______|\t\u2551")
        print("\u2551\t\t\t\t\t\t\t\t\t\u2551")
        print("\u2551\t\t\t\tVERSENKEN\t\t\t\t\u2551")
        print("\u255A",end='')
        while i > 0:
            print("\u2550", end='')
            i=i-1
        print("\u255D",end='')
        print()

    def print_menu(self):
        """
        Gibt Menu aus: 1 - Neues Spiel
                       2 - Lade Spiel
        """
        
    def clear_terminal(self):
        """
        Löscht Inhalt der Shell
        """
        if platform.system() == "Windows":
            os.system('cls')
        if platform.system() == "Linux":
            os.system('clear')


def main(_argv):
    """
    Hauptfunktion
    Args:
        _argv ([type]): [description]
    """
    master: Master = Master()
    master.print_willkommensnachricht()
    time.sleep(3)
    master.clear_terminal()
    master.print_spielfeld()


if __name__ == '__main__':
    main(sys.argv)
