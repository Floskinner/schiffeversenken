"""
Masterdatei fuer das Spiel Schiffe versenken
"""
from typing import Optional

import sys
import os
import platform
import time
import keyboard


from schiffeversenken import Farben, Rahmenzeichen, Richtung, Status, __schiffe__
from .schiff import Schiff
from .koordinate import Koordinate
from .spieler import Spieler
from .spielfeld import Spielfeld
from .helferklasse import speichern, laden, user_input


class Master:
    """Klasse die das ganze Spiel verwaltet und steuert
    """

    def __init__(self):
        self.__ist_spiel_vorbei = False

        self.__speichern_flag = False

        self.__spieler_1: Optional[Spieler] = None
        self.__spieler_2: Optional[Spieler] = None

        self.__aktueller_gegner: Optional[Spieler] = None
        self.__aktueller_spieler: Optional[Spieler] = None

        keyboard.add_hotkey('ctrl+s', self.__setzte_speichern_flag, args=(), suppress=True, timeout=1, trigger_on_release=False)

    @property
    def speichern_flag(self) -> bool:
        """
        Getter für speichern_flag
        """
        return self.__speichern_flag

    @property
    def ist_spiel_vorbei(self) -> bool:
        """
        Getter für ist_spiel_vorbei
        """
        return self.__ist_spiel_vorbei

    @property
    def spieler_1(self) -> Spieler:
        """
        Getter für Spieler_1
        """
        return self.__spieler_1

    @spieler_1.setter
    def spieler_1(self, spieler_1: Spieler):
        """
        Setter fuer den Spieler 1
        """
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
        """
        Setter fuer den Spieler 2
        """
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
        """Setter fuer aktueller_spieler

        Args:
            aktueller_spieler (Spieler): aktueller Spieler
        """
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

    @staticmethod
    def print_willkommensnachricht():
        """
        Gibt Willkommensnachricht aus
        """
        print("\t\t\t\t\u2554", end='')
        i = 0
        while i < 71:
            print("\u2550", end='')
            i = i+1
        print("\u2557", end='')
        print()
        print("\t\t\t\t\u2551\t  _____              _          _      ___   ___\t\t\u2551")
        print("\t\t\t\t\u2551\t / ____|            | |        |_|    / __| / __|   ___\\ \t\u2551")
        print("\t\t\t\t\u2551\t| (___       ____   | |___      _    | |__  | |__  / __ \\\t\u2551")
        print("\t\t\t\t\u2551\t\\___  \\    /  __|   |     \\    | |   |  __| | ___|| |__|_|\t\u2551")
        print("\t\t\t\t\u2551\t ____) |  |  (___   |  __  |   | |   | |    | |   | |_____\t\u2551")
        print("\t\t\t\t\u2551\t|_____/    \\____|   |_|  |_|   |_|   |_|    |_|   \\______|\t\u2551")
        print("\t\t\t\t\u2551\t\t\t\t\t\t\t\t\t\u2551")
        print("\t\t\t\t\u2551\t\t\t\tVERSENKEN\t\t\t\t\u2551")
        print("\t\t\t\t\u255A", end='')
        while i > 0:
            print("\u2550", end='')
            i = i-1
        print("\u255D", end='')
        print()

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

    @staticmethod
    def __print_zeile(zeile):
        j = 0
        cnt_spalten = len(zeile)
        for feld in zeile:
            if feld == Status.WASSER:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}   ", end='')
            elif feld == Status.SCHIFF:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {Farben.GRUEN.value}#{Farben.FARB_ENDE.value} ", end='')
            elif feld == Status.TREFFER:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {Farben.ROT.value}X{Farben.FARB_ENDE.value} ", end='')
            elif feld == Status.DANEBEN:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {Farben.BLAU.value}O{Farben.FARB_ENDE.value} ", end='')
            else:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {feld} ", end='')

            if cnt_spalten == 11 and j == 10:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")
            if j == 9 and not cnt_spalten == 11:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")
            j = j+1

    @staticmethod
    def __print_trennlinie():
        i = 0
        print("\t\t\t\t", end='')
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}", end='')
        while i < 43:
            print(f"{Rahmenzeichen.HEAVY_HORIZONTAL.value}", end='')
            i = i+1
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")

    @staticmethod
    def __print_rahmen_oben():
        # Erste Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u250F", end='')
        while i < 43:
            print(f"{Rahmenzeichen.HEAVY_HORIZONTAL.value}", end='')
            i = i+1
        print("\u2513")

    @staticmethod
    def __print_rahmen_unten():
        # Letzte Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u2517", end='')
        while i < 43:
            print(f"{Rahmenzeichen.HEAVY_HORIZONTAL.value}", end='')
            i = i+1
        print("\u251B")

    @staticmethod
    def __get_zeilen_von_spielfeld(spielfeld: Spielfeld) -> list[list[Status]]:
        zeilen: list[list[Status]] = list()
        for row in range(len(spielfeld.spielfeld)):
            zeile: list[Status] = list()
            for column in range(len(spielfeld.spielfeld[row])):
                zeile.append(spielfeld.spielfeld[column][row])
            zeilen.append(zeile)
        return zeilen

    @staticmethod
    def clear_terminal():
        """
        Löscht Inhalt der Shell
        """
        if platform.system() == "Windows":
            os.system('cls')
        if platform.system() == "Linux":
            os.system('clear')

    @staticmethod
    def print_countdown(zeit: int = 3):
        """Zaehle einen Countdown herunter

        Args:
            zeit (int, optional): Die Sekunden die, der Countdown brauchen soll. Defaults to 3.
        """
        while zeit:
            print(f"\t\t\t\tAnzeige wird in {zeit} Sekunden geloescht.")
            time.sleep(1)
            zeit -= 1

    @staticmethod
    def __print_spielende(gewinner: Spieler):
        """Gibt eine Nachricht aus, die den Gewinner verkündet und das Spiel beendet
        """
        print(f"\t\t\t\t{gewinner.name} hat gewonnen! Glueckwunsch!")

    @staticmethod
    def print_menu() -> int:
        """Ausgabe des Menus und Einlesen einer gueltigen Option

        Returns:
            int: gewaehlte Option
        """
        print("\t\t\t\tMenu:")
        auswahl = user_input("\t\t\t\t1 - Neues Spiel\n\t\t\t\t2 - Spiel laden\t\t", int(), (1, 2))
        return auswahl

    def __print_alles_fuer_spielzug(self):
        print(f"\t\t\t\t{self.aktueller_spieler.name} du bist dran.\n")
        print("\t\t\t\tHier hast du schon ueberall hingeschossen: ")
        self.print_spielfeld(self.aktueller_spieler.spielfeld_gegner)
        print("\n\t\t\t\tEigenes Spielfeld:")
        self.print_spielfeld(self.aktueller_spieler.spielfeld)
        print(f"\t\t\t\t{self.aktueller_spieler.name}, wo willst du hinschiessen?")

    def neues_spiel(self):
        """Für jeden Spieler den Namen einlesen, Schiffe platzieren
        """
        spieler = list()
        for spieler_nummer in range(1, 3):
            self.clear_terminal()
            name_spieler = self.get_user_input_name(spieler_nummer)
            spielfeld_spieler = Spielfeld()
            for schiff in __schiffe__:
                ist_platziert = False
                while not ist_platziert:
                    try:
                        self.clear_terminal()
                        self.print_spielfeld(spielfeld_spieler)
                        print(f"\t\t\t\t{name_spieler}, platziere {schiff.name} mit Groesse {schiff.groeße}:")
                        koordinate: Koordinate = self.get_user_input_koordinate()
                        richtung: Richtung = self.get_user_input_richtung()
                        koordinate.richtung = richtung
                        self.platziere_schiff(spielfeld_spieler, schiff, koordinate)
                        ist_platziert = True
                    except IndexError:
                        print("Das Schiff kann so nicht platziert werden. Leertaste fuer weiter.")
                        keyboard.wait(hotkey='space')  # enter=28  space=57
                        ist_platziert = False
                    except ValueError:
                        print("Ungueltige Eingabe. Leertaste fuer weiter.")
                        keyboard.wait(hotkey='space')  # enter=28  space=57
            spieler.append(Spieler(name_spieler, spielfeld_spieler, Spielfeld(), 0))

        self.spieler_1 = spieler[0]
        self.spieler_2 = spieler[1]
        self.clear_terminal()

    def __toggle_spielzug(self):
        """Tausche aktueller_spieler und aktueller_gegner
        """
        temp: Spieler = self.aktueller_spieler
        self.aktueller_spieler = self.aktueller_gegner
        self.aktueller_gegner = temp

    def __speicher_spielstand_daten(self) -> dict:
        """Sammelt die benoetigten Daten der Aktuellen Spieler und gibt diese zurueck

        Returns:
            dict: fertiges dict zum speichern
        """
        daten: dict = {}

        # Allgemeine Daten wie Name und Punkte
        daten["master"] = {
            "aktueller_spieler": {
                "name": self.aktueller_spieler.name,
                "punkte": self.aktueller_spieler.punkte
            },
            "aktueller_gegner": {
                "name": self.aktueller_gegner.name,
                "punkte": self.aktueller_gegner.punkte
            }
        }

        # Spielfeder fuer aktueller Spieler
        daten[self.aktueller_spieler.name] = {
            "spielfeld": self.aktueller_spieler.spielfeld.spielfeld,
            "spielfeld_gegner": self.aktueller_spieler.spielfeld_gegner.spielfeld
        }

        # Spielfeder fuer aktueller gegner Spieler
        daten[self.aktueller_gegner.name] = {
            "spielfeld": self.aktueller_gegner.spielfeld.spielfeld,
            "spielfeld_gegner": self.aktueller_gegner.spielfeld_gegner.spielfeld
        }

        return daten

    def __speicher_spielstand(self):
        """Fragt den User nach einem Pfad und speichert diesen am angegeben Ort. Wenn String leer, dann aktueller Pfad
        """
        try:
            pfad = user_input("\t\t\t\tPfad zum Speichern (optional auch leer):", str)
            daten = self.__speicher_spielstand_daten()
            speichern(daten, pfad)
        except IOError:
            print("\t\t\t\tSpielstand konnte nicht gespeichert werden! Pls try again")
            self.__speicher_spielstand()

    def __lade_spielstand(self, pfad: str):
        try:
            daten: dict = laden(pfad)

            aktueller_spieler_master = daten["master"]["aktueller_spieler"]
            aktueller_spieler_gegner_master = daten["master"]["aktueller_gegner"]

            aktueller_spieler_name = aktueller_spieler_master["name"]
            aktueller_spieler_punkte = aktueller_spieler_master["punkte"]
            aktueller_spieler_spielfeld = Spielfeld(spielfeld=daten[aktueller_spieler_name]["spielfeld"])
            aktueller_spieler_spielfeld_gegner = Spielfeld(spielfeld=daten[aktueller_spieler_name]["spielfeld_gegner"])

            aktueller_spieler_gegner_name = aktueller_spieler_gegner_master["name"]
            aktueller_spieler_gegner_punkte = aktueller_spieler_gegner_master["punkte"]
            aktueller_spieler_gegner_spielfeld = Spielfeld(spielfeld=daten[aktueller_spieler_gegner_name]["spielfeld"])
            aktueller_spieler_gegner_spielfeld_gegner = Spielfeld(spielfeld=daten[aktueller_spieler_gegner_name]["spielfeld_gegner"])

            self.aktueller_spieler = Spieler(aktueller_spieler_name, aktueller_spieler_spielfeld,
                                             aktueller_spieler_spielfeld_gegner, aktueller_spieler_punkte)
            self.aktueller_gegner = Spieler(aktueller_spieler_gegner_name, aktueller_spieler_gegner_spielfeld,
                                            aktueller_spieler_gegner_spielfeld_gegner, aktueller_spieler_gegner_punkte)

        except KeyError:
            print("\t\t\t\tGespeicherte Datei wurde beschaedigt, spielstand konnte nicht wiederhergestellt werden!")
            sys.exit(1)
        except (IOError, FileNotFoundError, TypeError):
            print("\t\t\t\tFehler beim Laden der Daten! Bitte neu versuchen")
            sys.exit(1)

    def __setzte_speichern_flag(self, zusandt: bool = True):
        """Beim Beenden des aktuellen Zuges sorgt diese Flag, dass der Spielstand gespeichert wird

        Args:
            zusandt (bool, optional): Defaults to True.
        """
        self.__speichern_flag = zusandt

    @staticmethod
    def schiessen(spieler: Spieler, gegner: Spieler, koordinate: Koordinate) -> Status:
        """Schuss auf Koordinate.

        Args:
            spieler (Spieler): Angreifer
            gegner (Spieler): Gegner
            koordinate (Koordinate): Wohin geschossen werden soll

        Returns:
            Status: Status des Treffers
        """
        try:
            schuss_ergebnis: Status = gegner.wird_abgeschossen(koordinate)
            if schuss_ergebnis == Status.TREFFER:
                spieler.update_spielfeld_gegner(koordinate, Status.TREFFER)
                gegner.update_spielfeld(koordinate, Status.TREFFER)
                return Status.TREFFER
            spieler.update_spielfeld_gegner(koordinate, Status.DANEBEN)
            return Status.DANEBEN
        except IndexError:
            return Status.UNGUELTIG

    @staticmethod
    def get_user_input_koordinate() -> Koordinate:
        """Abfrage Koordinate von Konsole

        Returns:
            Koordinate: koordinate
        """
        koordinate = user_input("\n\t\t\t\tGebe eine Koordinate ein: ", str)
        buchstabe = koordinate[0]
        zahl = int(koordinate[1:])
        return Koordinate(buchstabe, zahl)

    @staticmethod
    def get_user_input_richtung() -> Richtung:
        """Abfrage der Richtung in die das Schiff platziert werden soll.

        Returns:
            Richtung: richtung
        """
        return Richtung(user_input("\n\t\t\t\tWaehle Richtung:\n """
                                   "\t\t\t\t0 - Norden\n"""
                                   "\t\t\t\t1 - Osten\n"""
                                   "\t\t\t\t2 - Sueden\n"""
                                   "\t\t\t\t3 - Westen\n"""
                                   "\t\t\t\t", int()))

    @staticmethod
    def get_user_input_name(spieler_nummer: int) -> str:
        """Abfrage eines Spielernamens von Konsole

        Args:
            spieler_nummer (int): Spieler, der gerade dran ist

        Returns:
            str: Spielername des Spielers
        """
        return user_input(f"\n\t\t\t\tName von Spieler {spieler_nummer}: ", str)

    @staticmethod
    def platziere_schiff(spielfeld: Spielfeld, schiff: Schiff, koordinate: Koordinate):
        """Uebergebenes Schiff wird platziert

        Args:
            spielfeld (Spielfeld): das Spielfeld, wo das Schiff platziert werden soll
            schiff (Schiff): das Schiff, welches platziert werden soll
            koordinate (Koordinate): Koordinate und Richtung, wo das Schiff platziert werden soll

        Returns:
            Spielfeld: Spielfeld mit platziertem Schiff
        """
        spielfeld.plaziere_schiff(koordinate, schiff)

    def spielen(self):
        """Methode die nach dem Initalisieren aufgerufen werden kann, damit die normale Spielabfolge bis zu einem gewinner ausgeführt werden kann
        """
        self.clear_terminal()
        self.__print_alles_fuer_spielzug()
        koordinate: Koordinate = self.get_user_input_koordinate()
        gueltiger_schuss: bool = False

        while not gueltiger_schuss:
            gueltiger_schuss = self.fuehre_spielzug_aus(koordinate)

        self.print_countdown(5)

        if self.__speichern_flag:
            self.__speicher_spielstand()
            self.__setzte_speichern_flag(False)

        if self.__ist_spiel_vorbei:
            self.__print_spielende(self.aktueller_spieler)

        self.__toggle_spielzug()

    def fuehre_spielzug_aus(self, koordinate: Koordinate) -> bool:
        """Spielzug (Schuss) ausfuehren.

        Args:
            koordinate (Koordinate): Wohin geschossen werden soll.

        Returns:
            bool: ob Koordinate gueltig
        """
        schuss_ergebnis: Status = self.schiessen(self.aktueller_spieler, self.aktueller_gegner, koordinate)
        if schuss_ergebnis == Status.TREFFER:
            print("\t\t\t\tTreffer!")
            self.__ist_spiel_vorbei = self.aktueller_gegner.is_tot()
            return True
        if schuss_ergebnis == Status.DANEBEN:
            print("\t\t\t\tDaneben!")
            return True
        print("\t\t\t\tUngueltige Koordinate!")
        return False

    def initialisieren(self, auswahl: int):
        """Bereitet die Klasse mit allen noetigen Initalisierungen vor, damit gespielt werden kann

        Args:
            auswahl (int): 1 = Neus Spiel, 2 = Spiel Laden
        """
        if auswahl == 1:
            self.neues_spiel()
            self.aktueller_spieler = self.spieler_1
            self.aktueller_gegner = self.spieler_2
        elif auswahl == 2:
            pfad: str = user_input("\t\t\t\tPfad zum Spielstand: ", str)
            self.__lade_spielstand(pfad)
