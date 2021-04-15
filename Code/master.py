"""[DocString]
"""
from schiff import Schiff
from koordinate import Koordinate
from spieler import Spieler
from spielfeld import Spielfeld
from helferklasse import Rahmenzeichen, Status
import sys
import os
import platform
import time


class Master:
    """[summary]
    """

    erlaubte_buchstaben:list = ["A","B","C","D","E","F","G","H","I","J"]

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
    def aktueller_spieler(self, aktueller_spieler:Spieler):
        self.__aktueller_spieler = aktueller_spieler

    @property
    def aktueller_gegner(self) -> Spieler:
        return self.__aktueller_gegner
    
    @aktueller_gegner.setter
    def aktueller_gegner(self, aktueller_gegner:Spieler):
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
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} # ", end='')
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
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}", end='')
        while i < 43:
            print("\u2501", end='')
            i = i+1
        print(f"{Rahmenzeichen.HEAVY_VERTICAL.value}")

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
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {cnt_zeile}", end='')
            else:
                print(f"{Rahmenzeichen.HEAVY_VERTICAL.value} {cnt_zeile} ", end='')
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
        name_spieler_1 = input("Name von Spieler 1: ")
        self.__spieler_1 = Spieler(name_spieler_1, Spielfeld(), Spielfeld(), 0)        
        name_spieler_2 = input("Name von Spieler 2: ")
        self.__spieler_2 = Spieler(name_spieler_2,Spielfeld(),Spielfeld(),0)

    def toggle_spielzug(self):
        if self.aktueller_spieler == self.__spieler_1:
            self.aktueller_spieler == self.__spieler_2
            self.aktueller_gegner == self.__spieler_1
        elif self.aktueller_spieler == self.__spieler_2:
            self.aktueller_spieler == self.__spieler_1
            self.aktueller_gegner == self.__spieler_2

    def print_countdown(self, zeit: int = 3):
        while zeit:
            print(f"Anzeige wird in {zeit} Sekunden geloescht.")
            time.sleep(1)
            zeit -= 1

    def print_spielende(self):
        """Gibt eine Nachricht aus, die den Gewinner verkündet und das Spiel beendet
        """
    def schiessen(self, spieler: Spieler, gegner: Spieler):
        print(f"{spieler.name}, wo willst du hinschiessen?")
        koordinate:Koordinate = self.get_user_input_koordinate()
        schuss_ergebnis:int = spieler.wird_abgeschossen(koordinate)
        if schuss_ergebnis == 1:
            print("Treffer!")
            spieler.update_spielfeld_gegner(koordinate, Status.TREFFER)
            gegner.update_spielfeld(koordinate, Status.TREFFER)
        elif schuss_ergebnis == -1:
            print("Daneben!")
            spieler.update_spielfeld_gegner(koordinate, Status.DANEBEN)

    def get_user_input_koordinate(self)->Koordinate:
        ist_buchstabe_erlaubt = False
        while not ist_buchstabe_erlaubt:
            buchstabe = input("Geben Sie den Buchstabenwert der Koordinate ein: ")
            if buchstabe in self.erlaubte_buchstaben:
                ist_buchstabe_erlaubt = True
            else:                
                print("Keine gültige Eingabe.")
        
        ist_zahl_erlaubt = False
        while not ist_zahl_erlaubt:
            zahl = input("Geben Sie den Zahlenwert der Koordinate ein: ")
            if self.__ist_int(zahl):
                if int(zahl) <= 10 and int(zahl) > 0:
                    zahl = int(zahl)
                    ist_zahl_erlaubt = True
                else:
                    print("Die Zahl muss größer als 0 und kleiner als 11 sein.") 
            else:
                print("Die Eingabe war keine ganze Zahl.")
        return Koordinate(buchstabe, zahl)          
                
    def __ist_int(self, zahl) -> bool:
        try:
            int(zahl)
            return True
        except ValueError:
            return False

    def platziere_schiffe(self)->Spielfeld:
        schiffe:list = [Schiff("Schlachtschiff",5),
        Schiff("Kreuzer",4), Schiff("Kreuzer",4), 
        Schiff("Zerstoerer",3), Schiff("Zerstoerer",3),Schiff("Zerstoerer",3),
        Schiff("U-Boot",2),Schiff("U-Boot",2),Schiff("U-Boot",2),Schiff("U-Boot",2)]

        for schiff in schiffe:
            self.print_spielfeld(self.aktueller_spieler.spielfeld)
            print(f"{self.aktueller_spieler.name}, platziere {schiff.name} mit Groesse {schiff.groeße}:")
            ist_platziert = False
            while(not ist_platziert):
                koordinate:Koordinate = self.get_user_input_koordinate()
                richtung = input("Waehle Richtung:\n0 - Norden\n1 - Osten\n2 - Sueden\n3 - Westen\n")
                if self.__ist_int(richtung) and int(richtung) >= 0 and int(richtung) <= 3:                                  
                    try:
                        self.aktueller_spieler.spielfeld.plaziere_schiff(koordinate, int(richtung), schiff)
                        self.clear_terminal()
                        ist_platziert = True
                    except IndexError:
                        print("Das Schiff kann so nicht platziert werden.")
                        ist_platziert = False
                else:
                    print("Ungueltige Eingabe.")

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
        auswahl = input("1 - Neues Spiel\n2 - Spiel laden\n")
        if self.__ist_int(auswahl):
            return int(auswahl)

    def print_alles_fuer_spielzug(self):
        print(f"{self.aktueller_spieler.name} du bist dran.\n")
        print("Hier hast du schon ueberall hingeschossen: ")
        self.print_spielfeld(self.aktueller_spieler.spielfeld_gegner)
        print("\nEigenes Spielfeld")
        self.print_spielfeld(self.aktueller_spieler.spielfeld)
        self.schiessen(self.aktueller_spieler, self.aktueller_gegner)


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

    auswahl: int = master.print_menu()
    if auswahl == 1:
        master.neues_spiel()
        master.aktueller_spieler = master.spieler_1
        master.aktueller_gegner = master.spieler_2
        master.platziere_schiffe()
        master.toggle_spielzug()
        master.platziere_schiffe()
        master.toggle_spielzug()
    elif auswahl == 2:
        pass
    master.clear_terminal()
        
    spiel_vorbei:bool = False
    while not spiel_vorbei:
        master.print_alles_fuer_spielzug()
        master.print_countdown(3)
        master.toggle_spielzug()


if __name__ == '__main__':
    main(sys.argv)
