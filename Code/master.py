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
    @property
    def spieler_1(self)->Spieler:
        """
        Getter für Spieler_1
        """
        return self.__spieler_1

    def __print_zeile(self, daten):
        j = 0
        cnt_spalten = len(daten)
        for feld in daten:
            if feld == 0:
                print(f"\u2503   ", end='')
            elif feld == 2:
                print(f"\u2503 # ", end='')
            elif feld == 1:
                print(f"\u2503 X ", end='')
            elif feld == -1:
                print(f"\u2503 O ", end='')
            else:
                print(f"\u2503 {feld} ", end='')

            if cnt_spalten == 11 and j == 10:
                print("\u2503")
            if j == 9 and not cnt_spalten == 11:
                print("\u2503")
            j = j+1

    def __print_trennlinie(self):
        i = 0
        print("\u2503", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u2503")

    def __print_rahmen_oben(self):
        # Erste Zeile des Spielfelds
        i = 0
        print("\u250F", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u2513")

    def __print_rahmen_unten(self):
        # Erste Zeile des Spielfelds
        i = 0
        print("\u2517", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u251B")

    def __get_zeilen_von_spielfeld(self, spielfeld: Spielfeld) -> list:
        neues_array: list = list()
        for y in range(len(spielfeld.spielfeld)):
            zeile: list = list()
            for x in range(len(spielfeld.spielfeld[y])):
                zeile.append(spielfeld.spielfeld[x][y])
            neues_array.append(zeile)
        return neues_array

    def print_spielfeld(self, spielfeld: Spielfeld):
        """
        Gibt Spielfeld aus.
        """
        # Headerzeile
        self.__print_rahmen_oben()
        self.__print_zeile([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.__print_trennlinie()
        cnt_zeile = 1
        # Drehe Spielfeld, damit man es einfacher zeichnen kann
        gedrehtes_spielfeld = self.__get_zeilen_von_spielfeld(spielfeld)

        for zeile in gedrehtes_spielfeld:
            if cnt_zeile == 10:
                print(f"\u2503 {cnt_zeile}", end='')
            else:
                print(f"\u2503 {cnt_zeile} ", end='')
            self.__print_zeile(zeile)
            if cnt_zeile < 10:
                self.__print_trennlinie()
            else:
                self.__print_rahmen_unten()
            cnt_zeile = cnt_zeile+1

    def neues_spiel(self):
        """
        Erstellt leeres Spielfeld,
        fragt Spielernamen ab            
        """
    def print_countdown(self, zeit:int=3):
        pass

    def print_spielende(self):
        """Gibt eine Nachricht aus, die den Gewinner verkündet und das Spiel beendet
        """
    def schiessen(spieler:Spieler, gegner:Spieler):
        pass

    def platziere_schiffe

    def print_willkommensnachricht(self):
        """
        Gibt Willkommensnachricht aus
        """
        print("\u2554", end='')
        i = 0
        while i < 71:
            print("\u2550", end='')
            i = i+1
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
        print("\u255A", end='')
        while i > 0:
            print("\u2550", end='')
            i = i-1
        print("\u255D", end='')
        print()

    def print_menu(self) -> int:
        """
        Gibt Menu aus: 1 - Neues Spiel
                       2 - Spiel laden
        """
        print("Menu:")
        input("1 - Neues Spiel\n2 - Spiel laden\t")

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
    auswahl: int = master.print_menu()
    master.clear_terminal()
    spielfeld = Spielfeld()
    master.print_spielfeld(spielfeld)
    master.print_spielfeld(spielfeld)


if __name__ == '__main__':
    main(sys.argv)
