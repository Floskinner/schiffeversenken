"""Entahelt die Klasse Spielfeld fuer das Spiel Schiffeversenken
"""

from typing import Optional, Union

from schiffeversenken import Status, Richtung
from .koordinate import Koordinate
from .schiff import Schiff


class Spielfeld():
    """Klasse womit ein Spielfeld für 1 Person erstellt und verwaltet werden kann
    """

    def __init__(self, **kwargs: Union[int, list[list[int]], list[list[Status]]]):
        """Erstelle Spielfeld
        kwargs (dict):
            dimension (int) = 10: Veraendert die groesse vom Spielfeld
            spielfeld list[list[int]]]: Fertiges Spielfeld zuordnen
            spielfeld list[list[Status]]: Fertiges Spielfeld zuordnen
        """

        dimension: Optional[int] = None
        self.__spielfeld: Optional[list[list[int]]] = None

        dimension = kwargs.get("dimension")
        self.__spielfeld = kwargs.get("spielfeld")

        if dimension is None:
            dimension = 10

        if self.__spielfeld is None:
            self.__spielfeld = [Status.WASSER] * dimension

            for x_position in range(dimension):
                self.__spielfeld[x_position] = [Status.WASSER] * dimension

    @property
    def spielfeld(self) -> list[list[int]]:
        """Getter fuer Spielfeld

        Returns:
            list[list[int]]: Spielfeld
        """
        return self.__spielfeld

    @spielfeld.setter
    def spielfeld(self, spielfeld: list[list[int]]):
        """Setter fuer Spielfeld

        Args:
            spielfeld (list[list[int]]): Spielfeld
        """
        self.__spielfeld = spielfeld

    def set_feld(self, status: Status, koordinate: Koordinate):
        """Setzt den Satus eines bestimmten Feldes

        Args:
            staus (Status): daneben, neutral, treffer, Schiff
            koordinate (Koordinate): Position
        """
        self.__spielfeld[koordinate.x_position][koordinate.y_position] = status

    def plaziere_schiff(self, koordinate: Koordinate, schiff: Schiff):
        """
        Plaziert das Schiff auf der Angegebenen Position in die entsprechende Richtung
        Rais: IndexError

        Args:
            koordinate (Koordinate): Startpunkt mit Richtung
            schiff (Schiff): Das zu plazierende Schiff
        """
        # Ermittle alle Koordinaten wo das Schiff sein wird
        koordinaten_schiff = self.__get_koordinaten_in_richtung(koordinate, schiff.groeße)

        # Checke ob das Schiff platziert werden darf
        for koordinate_schiff in koordinaten_schiff:
            if not self.__valides_plazieren(koordinate_schiff):
                raise IndexError(
                    f"Das Schiff kann so nicht plaziert werden! Start:{koordinate.x_position},{koordinate.y_position} Richtung:{koordinate.richtung}")

        # Plaziere Schiff
        for koordinate_schiff in koordinaten_schiff:
            self.set_feld(Status.SCHIFF, koordinate_schiff)

    def get_status_bei(self, koordinate: Koordinate) -> Status:
        """
        Gibt den Status des Feldes an der entsprechenden Position zurueck

        Args:
            koordinate (Koordinate): Position welche ueberprueft wird

        Returns:
            Status: daneben, asser, treffer, Schiff
        """
        return self.__spielfeld[koordinate.x_position][koordinate.y_position]

    def alle_schiffe_zerstoert(self) -> bool:
        """Zum uberpruefen ob ein Spieler verloren hat, bzw ob noch ein intaktes Schiffteil
        auf dem Spielfeld vorhanden ist

        Returns:
            bool: True - Kein Schiffsteil mehr uebrig, False - Mindestens ein Teil uebrig
        """
        for x_felder in self.__spielfeld:
            for feld in x_felder:
                if feld == Status.SCHIFF:
                    return False
        return True

    def reset(self):
        """Setzt alle Felder auf den Wert 0
        """
        for x_position in range(len(self.__spielfeld)):
            for y_position in range(len(self.__spielfeld[0])):
                self.__spielfeld[x_position][y_position] = Status.WASSER

    def __valides_plazieren(self, koordinate: Koordinate) -> bool:
        """Checkt alle Felder um der entsprechendenKoordinate und schaut, ob dort ein Schiff plaziert ist

        Args:
            koordinate (Koordinate): Position

        Returns:
            bool: True - nur Wasser, False - nicht nur Wasser
        """
        koordinaten: list[Koordinate] = self.__get_koordinaten_drumherum(koordinate)

        if len(koordinaten) < 4:
            return False

        for valide_koordinate in koordinaten:
            tmp_status: Status = self.get_status_bei(valide_koordinate)
            if tmp_status != Status.WASSER:
                return False

        return True

    def __get_koordinaten_drumherum(self, koordinate: Koordinate) -> list[Koordinate]:
        """Gibt alle moeglichen Koordinaten um eine entsprechende Position inklusive die uebergebene Position selbst

        Args:
            koordinate (Koordinate): Position

        Returns:
            list: Mit allen validen Koordinaten
        """

        koordinaten = []

        x_start_position = koordinate.x_position-1
        y_start_position = koordinate.y_position-1

        max_index = len(self.__spielfeld) - 1

        for y_position in range(3):
            for x_position in range(3):

                x_index = x_start_position+x_position
                y_index = y_start_position+y_position

                if 0 <= x_index <= max_index and 0 <= y_index <= max_index:
                    tmp_koordinate = Koordinate(x_index+1, y_index+1)
                    koordinaten.append(tmp_koordinate)

        return koordinaten

    @staticmethod
    def __get_koordinaten_in_richtung(koordinate: Koordinate, anzahl_felder: int) -> list:
        """Gibt die Koordinaten an, in welcher sich ein Schiff theoretisch befinden wird

        Args:
            koordinate (Koordinate): Start Position mit Richtung
            anzahl_felder (int): wie weit in die Richtung gegangen wird

        Returns:
            list[Koordinate]: Alle Koordinaten
        """
        koordinaten_schiff = []
        richtung = koordinate.richtung

        # Norden
        if richtung == Richtung.NORDEN:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinate.x_position
                y_position = koordinate.y_position - y_position_counter

                tmp_koordinate = Koordinate(x_position+1, y_position+1)
                koordinaten_schiff.append(tmp_koordinate)

        # Osten
        elif richtung == Richtung.OSTEN:
            for x_position_counter in range(anzahl_felder):

                x_position = koordinate.x_position + x_position_counter
                y_position = koordinate.y_position

                tmp_koordinate = Koordinate(x_position+1, y_position+1)
                koordinaten_schiff.append(tmp_koordinate)

        # Sueden
        elif richtung == Richtung.SUEDEN:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinate.x_position
                y_position = koordinate.y_position + y_position_counter

                tmp_koordinate = Koordinate(x_position+1, y_position+1)
                koordinaten_schiff.append(tmp_koordinate)

        # Westen
        elif richtung == Richtung.WESTEN:
            for x_position_counter in range(anzahl_felder):

                x_position = koordinate.x_position - x_position_counter
                y_position = koordinate.y_position

                tmp_koordinate = Koordinate(x_position+1, y_position+1)
                koordinaten_schiff.append(tmp_koordinate)

        return koordinaten_schiff
