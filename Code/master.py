"""[DocString]
"""
from spielfeld import Spielfeld
import sys
import os
import platform
import time

class Master:
    """[summary]
    """

    def print_zeile(self, daten):
        j=0
        for feld in daten:
            if feld == 0:
                print(f"\u2503 \u224B  ", end='')
            if j==9:
                print("\u2503")
            j=j+1

    def print_trennlinie(self):
        i=0
        print("\u2503", end='')
        while i<49:            
            print("\u2501", end='')
            i=i+1;
        print("\u2503")
    
    def print_rahmen_oben(self):       
        #Erste Zeile des Spielfelds
        i=0
        print("\u250F", end='')
        while i<49:            
            print("\u2501", end='')
            i=i+1;
        print("\u2513")
    
    def print_rahmen_unten(self):       
        #Erste Zeile des Spielfelds
        i=0
        print("\u2517", end='')
        while i<49:            
            print("\u2501", end='')
            i=i+1;
        print("\u251B") 

    def print_spielfeld(self):
        """
        Gibt Spielfeld aus.
        """
        print("\u224B\t\u2693\t\u2388\t\u2668")
        print()
        spielfeld:Spielfeld = Spielfeld()
        self.print_rahmen_oben()
        cnt_zeile = 0
        for zeile in spielfeld.spielfeld:       
            self.print_zeile(zeile)
            if cnt_zeile < 9:
                self.print_trennlinie()
            else:
                self.print_rahmen_unten()
            cnt_zeile = cnt_zeile+1

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
    time.sleep(1)
    master.clear_terminal()
    master.print_spielfeld()


if __name__ == '__main__':
    main(sys.argv)
