"""
Masterdatei fuer das Spiel Schiffe versenken
"""
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
                                Schiff("Zerstoerer", 3), Schiff(
                                    "Zerstoerer", 3), Schiff("Zerstoerer", 3),
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

    @staticmethod
    def __print_zeile(daten):
        j = 0
        cnt_spalten = len(daten)
        for feld in daten:
            if feld == Status.WASSER:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}   ", end='')
            elif feld == Status.SCHIFF:
                print(
                    f"{Rahmenzeichen.HEAVY_VERTICAL.value} {Farben.GRUEN.value}#{Farben.FARB_ENDE.value} ", end='')
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

    @staticmethod
    def __print_trennlinie():
        i = 0
        print("\t\t\t\t", end='')
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")

    @staticmethod
    def __print_rahmen_oben():
        # Erste Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u250F", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u2513")

    @staticmethod
    def __print_rahmen_unten():
        # Letzte Zeile des Spielfelds
        i = 0
        print("\t\t\t\t", end='')
        print("\u2517", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print("\u251B")

    @staticmethod
    def __get_zeilen_von_spielfeld(spielfeld: Spielfeld) -> list:
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
        self.__print_zeile(
            [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
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
                        print(
                            f"{name_spieler}, platziere {schiff.name} mit Groesse {schiff.groeße}:")
                        koordinate: Koordinate = self.get_user_input_koordinate()
                        richtung: Richtung = self.get_user_input_richtung()
                        koordinate.richtung = richtung
                        spielfeld_spieler = self.platziere_schiff(
                            name_spieler, spielfeld_spieler, schiff, koordinate)
                        ist_platziert = True
                    except IndexError:
                        print(
                            "Das Schiff kann so nicht platziert werden. Leertaste fuer weiter.")
                        keyboard.wait(hotkey='space')  # enter=28  space=57
                        ist_platziert = False
                    except ValueError:
                        print("Ungueltige Eingabe. Leertaste fuer weiter.")
                        keyboard.wait(hotkey=57)  # enter=28  space=57
            self.__spieler.append(
                Spieler(name_spieler, spielfeld_spieler, Spielfeld(), 0))

        self.spieler_1 = self.__spieler[0]
        self.spieler_2 = self.__spieler[1]
        self.clear_terminal()

    def toggle_spielzug(self):
        temp: Spieler = self.aktueller_spieler
        self.aktueller_spieler = self.aktueller_gegner
        self.aktueller_gegner = temp

    @staticmethod
    def print_countdown(zeit: int = 3):
        while zeit:
            print(f"Anzeige wird in {zeit} Sekunden geloescht.")
            time.sleep(1)
            zeit -= 1

    @staticmethod
    def print_spielende():
        """Gibt eine Nachricht aus, die den Gewinner verkündet und das Spiel beendet
        """

    @staticmethod
    def schiessen(spieler: Spieler, gegner: Spieler, koordinate: Koordinate) -> Status:
        try:
            schuss_ergebnis: Status = spieler.wird_abgeschossen(koordinate)
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
        koordinate = input("Gebe eine Koordinate ein: ").strip()
        buchstabe = koordinate[0]
        zahl = int(koordinate[1:])
        return Koordinate(buchstabe, zahl)

    @staticmethod
    def get_user_input_richtung() -> Richtung:
        return Richtung(int(input("Waehle Richtung:\n0 - Norden\n1 - Osten\n2 - Sueden\n3 - Westen\n").strip()))

    @staticmethod
    def get_user_input_name(spieler_nummer: int) -> str:
        return input(f"Name von Spieler {spieler_nummer}: ")

    def platziere_schiff(self, spielfeld: Spielfeld, schiff: Schiff, koordinate: Koordinate) -> Spielfeld:
        self.print_spielfeld(spielfeld)
        spielfeld.plaziere_schiff(koordinate, schiff)
        return spielfeld

    @staticmethod
    def print_willkommensnachricht():
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
        print(
            "\u2551\t| (___       ____   | |___      _    | |__  | |__  / __ \\\t\u2551")
        print(
            "\u2551\t\\___  \\    /  __|   |     \\    | |   |  __| | ___|| |__|_|\t\u2551")
        print("\u2551\t ____) |  |  (___   |  __  |   | |   | |    | |   | |_____\t\u2551")
        print(
            "\u2551\t|_____/    \\____|   |_|  |_|   |_|   |_|    |_|   \\______|\t\u2551")
        print("\u2551\t\t\t\t\t\t\t\t\t\u2551")
        print("\u2551\t\t\t\tVERSENKEN\t\t\t\t\u2551")
        print("\u255A", end='')
        while i > 0:
            print("\u2550", end='')
            i = i-1
        print("\u255D", end='')
        print()

    @staticmethod
    def print_menu() -> int:
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

    @staticmethod
    def clear_terminal():
        """
        Löscht Inhalt der Shell
        """
        if platform.system() == "Windows":
            os.system('cls')
        if platform.system() == "Linux":
            os.system('clear')

    def __speicher_spielstand_daten(self) -> dict:
        """Sammelt die benoetigten Daten der Aktuellen Spieler und gibt diese zurueck

        Returns:
            dict: fertiges dict zum speichern
        """
        daten: dict = {}

        # Allgemeine Daten wie Name und Punkte
        daten["master"] = {
            "aktueller_spieler": {
                "name": self.__aktueller_spieler.name,
                "punkte": self.__aktueller_spieler.punkte
            },
            "aktueller_gegner": {
                "name": self.__aktueller_gegner.name,
                "punkte": self.__aktueller_gegner.punkte
            }
        }

        # Spielfeder fuer aktueller Spieler
        daten[self.__aktueller_spieler.name] = {
            "spielfeld": self.__aktueller_spieler.spielfeld,
            "spielfeld_gegner": self.__aktueller_spieler.spielfeld_gegner
        }

        # Spielfeder fuer aktueller gegner Spieler
        daten[self.__aktueller_gegner.name] = {
            "spielfeld": self.__aktueller_gegner.spielfeld,
            "spielfeld_gegner": self.__aktueller_gegner.spielfeld_gegner
        }

        return daten

    def __speicher_spielstand(self):
        """Fragt den User nach einem Pfad und speichert diesen am angegeben Ort. Wenn String leer, dann aktueller Pfad
        """

        pfad = input("Speicherpfad vom Spielstand (Leer - aktueller Pfad): ")
        daten = self.__speicher_spielstand_daten()
        if pfad.strip() == "":
            self.__speicherverwaltung.speichern(daten)
        else:
            self.__speicherverwaltung.speichern(daten, pfad)

    def __lade_spielstand(self, pfad: str):
        try:
            daten: dict = self.__speicherverwaltung.laden(pfad)

            aktueller_spieler_master = daten["master"]["aktueller_spieler"]
            aktueller_spieler_gegner_master = daten["master"]["aktueller_gegner"]

            aktueller_spieler_name = aktueller_spieler_master["name"]
            aktueller_spieler_punkte = aktueller_spieler_master["punkte"]
            aktueller_spieler_spielfeld = daten[aktueller_spieler_name]["spielfeld"]
            aktueller_spieler_spielfeld_gegner = daten[aktueller_spieler_name]["spielfeld_gegner"]

            aktueller_spieler_gegner_name = aktueller_spieler_gegner_master["name"]
            aktueller_spieler_gegner_punkte = aktueller_spieler_gegner_master["punkte"]
            aktueller_spieler_gegner_spielfeld = daten[aktueller_spieler_gegner_name]["spielfeld"]
            aktueller_spieler_gegner_spielfeld_gegner = daten[
                aktueller_spieler_gegner_name]["spielfeld_gegner"]

            self.__aktueller_spieler = Spieler(
                aktueller_spieler_name, aktueller_spieler_spielfeld, aktueller_spieler_spielfeld, aktueller_spieler_punkte)
            self.__aktueller_gegner = Spieler(aktueller_spieler_gegner_name, aktueller_spieler_gegner_spielfeld,
                                              aktueller_spieler_gegner_spielfeld, aktueller_spieler_gegner_punkte)

        except KeyError:
            print(
                "Gespeicherte Datei wurde beschaedigt, spielstand konnte nicht wiederhergestellt werden!")
            exit(self, 1)
        except:
            print("Fehler beim Laden der Daten! Bitte neu versuchen")
            exit(self, 1)

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
            pfad: str = input("Pfad zum Spielstand: ").strip()
            self.__lade_spielstand(pfad)
        
            
        spiel_vorbei:bool = False


        while not self.__ist_spiel_vorbei:
            self.clear_terminal()
            self.print_alles_fuer_spielzug()
            koordinate: Koordinate = self.get_user_input_koordinate()
            gueltiger_schuss: bool = False
            while not gueltiger_schuss:
                gueltiger_schuss = self.fuehre_spielzug_aus(koordinate)
            self.__ist_spiel_vorbei = self.__aktueller_gegner.is_tot()
            self.print_countdown(5)
            self.toggle_spielzug()
            if True:
                self.__speicher_spielstand()

    def fuehre_spielzug_aus(self, koordinate: Koordinate) -> bool:
        schuss_ergebnis: Status = self.schiessen(self.aktueller_spieler, self.aktueller_gegner, koordinate)
        if schuss_ergebnis == Status.TREFFER:
            print("Treffer!")
            return True
            
        if schuss_ergebnis == Status.DANEBEN:
            print("Daneben!")
            return True
        print("Ungueltige Koordinate!")
        return False


def main(_argv):
    master: Master = Master()
    master.spielen()


if __name__ == '__main__':
    main(sys.argv)
