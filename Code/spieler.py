from koordinate import Koordinate
from spielfeld import Spielfeld
from helferklasse import Status


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

    def update_spielfeld_gegner(self, koordinate: Koordinate, status: Status):
        """Aktualisieren des Gegner Spielfelds

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 
            status (Status): Status des Feldes
        """
        self.__spielfeld_gegner.set_feld(status, koordinate)

    def update_spielfeld(self, koordinate: Koordinate, status: Status):
        """Aktualisieren des eigenen Spielfelds

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 
            status (Status): Status des Feldes
        """
        self.__spielfeld.set_feld(status, koordinate)

    def add_punkt(self, punkte=1):
        """Hinzufügen eines Punktes
        """
        self.__punkte += punkte

    def wird_abgeschossen(self, koordinate: Koordinate) -> Status:
        """Prüfen und ändern der Felder des eigenen Spielfelds ob oder ob nicht getroffen wurde

        Args: 
            koordinate (Koordinate): Koordinate des Feldes 

        Returns:
            Status: daneben, Wasser, treffer, Schiff
        """

        status_feld = self.__spielfeld.get_status_bei(koordinate)

        if status_feld == Status.SCHIFF:
            self.__spielfeld.set_feld(Status.TREFFER, koordinate)

        return self.__spielfeld.get_status_bei(koordinate)

    @property
    def name(self) -> str:
        """Gibt Namen des Spielers zurück

        Returns:
            str: Name des Spielers
        """
        return self.__name

    @property
    def spielfeld(self) -> Spielfeld:
        """Gibt das Spielfeld zurück

        Returns:
            spielfeld 
        """
        return self.__spielfeld

    @property
    def spielfeld_gegner(self) -> Spielfeld:
        """Gibt den Spickzettel vom gegnerischen Spielfeld zurück

        Returns:
            spielfeld_gegner 
        """
        return self.__spielfeld_gegner
