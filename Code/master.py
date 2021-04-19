"""
Masterdatei fuer das Spiel Schiffe versenken
"""
from typing import List
import sys
import os
import platform
import time
import keyboard
from schiff import Schiff
from koordinate import Koordinate
from spieler import Spieler
from spielfeld import Spielfeld
from helferklasse import Farben, Rahmenzeichen, Richtung, Status, Speicherverwaltung


class Master:
    """[summary]
    """

    def __init__(self):
        self.__speicherverwaltung = Speicherverwaltung()
        self.__ist_spiel_vorbei = False
        self.__schiffe: list = [Schiff("Schlachtschiff", 5),
                                Schiff("Kreuzer", 4), Schiff("Kreuzer", 4),
                                Schiff("Zerstoerer", 3), Schiff("Zerstoerer", 3), Schiff("Zerstoerer", 3),
                                Schiff("U-Boot", 2), Schiff("U-Boot", 2), Schiff("U-Boot", 2), Schiff("U-Boot", 2)]
        self.__speichern_flag = False
        self.__spieler = list()

    @property
    def speichern_flag(self) -> bool:
        """
        Getter für speichern_flag
        """
        return self.__speichern_flag

    @property
    def spieler_1(self) -> Spieler:
        """
        Getter für Spieler_1
        """
        return self.__spieler_1

    @spieler_1.setter
    def spieler_1(self, spieler_1: Spieler):
        self.__spieler_1 = spieler_1

    @property
    def spieler_2(self) -> Spieler:
        """
        Getter für Spieler_2
        Returns:
            Spieler 
        """
        return self.__spieler_2

    @spieler_2.setter
    def spieler_2(self, spieler_2: Spieler):
        self.__spieler_2 = spieler_2

    @property
    def aktueller_spieler(self) -> Spieler:
        """
        Getter für aktuellen Spieler
        Returns:
            Spieler: Spieler, der gerade dran ist.
        """
        return self.__aktueller_spieler

    @aktueller_spieler.setter
    def aktueller_spieler(self, aktueller_spieler: Spieler):
        self.__aktueller_spieler = aktueller_spieler

    @property
    def aktueller_gegner(self) -> Spieler:
        """Getter fuer aktueller_gegner

        Returns:
            Spieler: aktueller_gegner
        """
        return self.__aktueller_gegner

    @aktueller_gegner.setter
    def aktueller_gegner(self, aktueller_gegner: Spieler):
        """Setter für aktuellen Gegner

        Args:
            aktueller_gegner (Spieler): Spieler, der gerade nicht dran ist.
        """
        self.__aktueller_gegner = aktueller_gegner

    def __print_zeile(self, daten):
        j = 0
        cnt_spalten = len(daten)
        for feld in daten:
            if feld == Status.WASSER:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}   ", end='')
            elif feld == Status.SCHIFF:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {Farben.GRUEN.value}#{Farben.FARB_ENDE.value} ", end='')
            elif feld == Status.TREFFER:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} X ", end='')
            elif feld == Status.DANEBEN:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} O ", end='')
            else:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {feld} ", end='')

            if cnt_spalten == 11 and j == 10:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")
            if j == 9 and not cnt_spalten == 11:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")
            j = j+1

    def __print_trennlinie(self):
        i = 0
        print("\t\t\t\t", end='')
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")

    def __print_rahmen_oben(self):
        # Erste Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u250F", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u2513")

    def __print_rahmen_unten(self):
        # Letzte Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u2517", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u251B")

    def __get_zeilen_von_spielfeld(self, spielfeld: Spielfeld) -> list:
        neues_array: list = list()
        for row in range(len(spielfeld.spielfeld)):
            zeile: list = list()
            for column in range(len(spielfeld.spielfeld[row])):
                zeile.append(spielfeld.spielfeld[column][row])
            neues_array.append(zeile)
        return neues_array

    def print_spielfeld(self, spielfeld: Spielfeld):
        """
        Gibt Spielfeld aus.
        """
        # Headerzeile
        self.__print_rahmen_oben()
        print("\t\t\t\t", end='')
        self.__print_zeile([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.__print_trennlinie()
        cnt_zeile = 1
        # Drehe Spielfeld, damit man es einfacher zeichnen kann
        gedrehtes_spielfeld = self.__get_zeilen_von_spielfeld(spielfeld)

        for zeile in gedrehtes_spielfeld:
            if cnt_zeile == 10:
                print("\t\t\t\t", end='')
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {cnt_zeile}", end='')

            else:
                print("\t\t\t\t", end='')
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {cnt_zeile} ", end='')

            self.__print_zeile(zeile)
            if cnt_zeile < 10:
                self.__print_trennlinie()
            else:
                self.__print_rahmen_unten()
            cnt_zeile = cnt_zeile+1

    def neues_spiel(self):
        """Für jeden Spieler den Namen einlesen, Schiffe platzieren

        Args:
            spieler_anzahl (int, optional): [description]. Defaults to 2.
        """
        for anzahl in range(1, 3):
            self.clear_terminal()
            name_spieler = self.get_user_input_name(anzahl)
            spielfeld_spieler = Spielfeld()
            for schiff in self.__schiffe:
                ist_platziert = False
                while not ist_platziert:
                    try:
                        self.clear_terminal()
                        self.print_spielfeld(spielfeld_spieler)
                        print(f"{name_spieler}, platziere {schiff.name} mit Groesse {schiff.groeße}:")
                        koordinate: Koordinate = self.get_user_input_koordinate()
                        richtung: Richtung = self.get_user_input_richtung()
                        koordinate.richtung = richtung
                        spielfeld_spieler = self.platziere_schiff(name_spieler, spielfeld_spieler, schiff, koordinate)
                        ist_platziert = True
                    except IndexError:
                        print("Das Schiff kann so nicht platziert werden. Leertaste fuer weiter.")
                        keyboard.wait(hotkey='space')  # enter=28  space=57
                        ist_platziert = False
                    except ValueError:
                        print("Ungueltige Eingabe. Leertaste fuer weiter.")
                        keyboard.wait(hotkey=57)  # enter=28  space=57
            self.__spieler.append(Spieler(name_spieler, spielfeld_spieler, Spielfeld(), 0))

        self.spieler_1 = self.__spieler[0]
        self.spieler_2 = self.__spieler[1]
        self.clear_terminal()

    def toggle_spielzug(self):
        temp: Spieler = self.aktueller_spieler
        self.aktueller_spieler = self.aktueller_gegner
        self.aktueller_gegner = temp

    def print_countdown(self, zeit: int = 3):
        while zeit:
            print(f"Anzeige wird in {zeit} Sekunden geloescht.")
            time.sleep(1)
            zeit -= 1

    def print_spielende(self):
        """Gibt eine Nachricht aus, die den Gewinner verkündet und das Spiel beendet
        """

    def schiessen(self, spieler: Spieler, gegner: Spieler, koordinate: Koordinate) -> Status:
        try:
            schuss_ergebnis: Status = spieler.wird_abgeschossen(koordinate)
            if schuss_ergebnis == Status.TREFFER:
                spieler.update_spielfeld_gegner(koordinate, Status.TREFFER)
                gegner.update_spielfeld(koordinate, Status.TREFFER)
                return Status.TREFFER
            else:
                spieler.update_spielfeld_gegner(koordinate, Status.DANEBEN)
                return Status.DANEBEN
        except IndexError:
            return Status.UNGUELTIG

    def get_user_input_koordinate(self) -> Koordinate:
        koordinate = input("Gebe eine Koordinate ein: ").strip()
        koordinate_list = koordinate.split()
        buchstabe = koordinate[0]
        zahl = int(koordinate[1:])
        return Koordinate(buchstabe, zahl)

    def get_user_input_richtung(self) -> Richtung:
        return Richtung(int(input("Waehle Richtung:\n0 - Norden\n1 - Osten\n2 - Sueden\n3 - Westen\n").strip()))

    def get_user_input_name(self, spieler_nummer: int) -> str:
        return input(f"Name von Spieler {spieler_nummer}: ")

    def platziere_schiff(self, name: str, spielfeld: Spielfeld, schiff: Schiff, koordinate: Koordinate) -> Spielfeld:
        self.print_spielfeld(spielfeld)
        spielfeld.plaziere_schiff(koordinate, schiff)
        return spielfeld

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
        ist_gueltig = False
        print("Menu:")
        while not ist_gueltig:
            auswahl = input("1 - Neues Spiel\n2 - Spiel laden\n")
            try:
                if isinstance(int(auswahl), int):
                    return int(auswahl)
            except ValueError:
                ist_gueltig = False

    def print_alles_fuer_spielzug(self):
        print(f"{self.aktueller_spieler.name} du bist dran.\n")
        print("Hier hast du schon ueberall hingeschossen: ")
        self.print_spielfeld(self.aktueller_spieler.spielfeld_gegner)
        print("\nEigenes Spielfeld:")
        self.print_spielfeld(self.aktueller_spieler.spielfeld)
        print(f"{self.aktueller_spieler.name}, wo willst du hinschiessen?")

    def clear_terminal(self):
        """
        Löscht Inhalt der Shell
        """
        if platform.system() == "Windows":
            os.system('cls')
        if platform.system() == "Linux":
            os.system('clear')

    def spielen(self):
        self.print_willkommensnachricht()
        time.sleep(3)
        self.clear_terminal()

        auswahl: int = self.print_menu()
        if auswahl == 1:
            self.neues_spiel()
            self.aktueller_spieler = self.spieler_1
            self.aktueller_gegner = self.spieler_2
        elif auswahl == 2:
            pass

        while not self.__spiel_vorbei:
            self.clear_terminal()
            self.print_alles_fuer_spielzug()
            koordinate: Koordinate = self.get_user_input_koordinate()
            gueltiger_schuss: bool = False
            while not gueltiger_schuss:
                gueltiger_schuss = self.fuehre_spielzug_aus(koordinate)
            self.__spiel_vorbei = self.__aktueller_gegner.is_tot()
            self.print_countdown(5)
            self.toggle_spielzug()
            if self.__speichern_flag:
                self.__speicherverwaltung.speichern()

    def fuehre_spielzug_aus(self, koordinate: Koordinate) -> bool:
        schuss_ergebnis: Status = self.schiessen(self.aktueller_spieler, self.aktueller_gegner, koordinate)
        if schuss_ergebnis == Status.TREFFER:
            print("Treffer!")
            return True
        elif schuss_ergebnis == Status.DANEBEN:
            print("Daneben!")
            return True
        elif schuss_ergebnis == Status.UNGUELTIG:
            print("Ungueltige Koordinate!")
            return False


def main(_argv):
    master: Master = Master()
    master.spielen()


if __name__ == '__main__':
    main(sys.argv)
