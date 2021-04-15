from koordinate import Koordinate
from spielfeld import Spielfeld

class Spieler:
    """Klasse womit ein Spieler verwaltet werden kann
    """
    def __init__(self, name: str, spielfeld: Spielfeld, spielfeld_gegner: Spielfeld, punkte: int = 0):
        """Erstelle Spieler

        Args: 
            name (str): Der Name des Spielers 
            spielfeld (Spieldfeld): Spielfeld des Spielers
            spielfeld_gegner (Spielfeld): Spielfeld des Gegners
            punkte (int): Punktestand der gewonnenen Spiele
        """
        self.__name = name
        self.__spielfeld = spielfeld
        self.__spielfeld_gegner = spielfeld_gegner
        self.__punkte = punkte

    def set_name(self, name: str):
        """Setzten des Spielernamens

        Args: 
            name (str): Der Name des Spielers 
        """
        self.__name = name

    def update_spielfeld_gegner(self, koordinate: Koordinate, status: int):
        """Aktualisieren des Gegner Spielfelds

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 
            status (int): Status des Feldes
        """
        self.__spielfeld_gegner.set_feld(status, koordinate)
        
    def update_spielfeld(self, koordinate: Koordinate, status: int = 1):
        """Aktualisieren des eigenen Spielfelds

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 
            status (int): Status des Feldes
        """
        self.__spielfeld.set_feld(status, koordinate)

    def add_punkt(self):
        """Hinzufügen eines Punktes
        """
        self.__punkte += 1
        
    def wird_abgeschossen(self, koordinate: Koordinate) -> int: 
        """Prüfen und ändern der Felder des eigenen Spielfelds ob oder ob nicht getroffen wurde

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 

        Returns:
            int: -1 daneben, 1 treffer
        """
        status_feld = self.__spielfeld.get_status_bei(koordinate)
        if status_feld == 1 or status_feld == 2:
            self.__spielfeld.set_feld(1, koordinate)
            return 1
        else:
            return -1

    def get_spielfeld(self) -> Spielfeld:
        """Gibt das Spielfeld zurück

        Returns:
            spielfeld 
        """
        return self.__spielfeld


    def set_spielfeld(self, spielfeld: Spielfeld):
        """Setzten des Spielfelds

        Args: 
            spielfeld (Spieldfeld): Spielfeld des Spielers

        Returns:
            spielfeld
        """
        self.__spielfeld = spielfeld