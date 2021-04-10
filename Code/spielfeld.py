"""Entahelt die Klasse Spielfeld fuer das Spiel Schiffeversenken
"""

from koordinaten import Koordinaten
from schiff import Schiff


class Spielfeld():
    """Klasse womit ein Spielfeld für 1 Person erstellt und verwaltet werden kann
    """

    def __init__(self, **kwargs):
        """Erstelle Spielfeld
        kwargs (dict):
            dimension (int) = 10: Veraendert die groesse vom Spielfeld
            spielfeld int[][]: Fertiges Spielfeld zuordnen
        """

        dimension = kwargs.get("dimension")
        self.__spielfeld: int = kwargs.get("spielfeld")

        if dimension is None:
            dimension = 10

        if self.__spielfeld is None:
            self.__spielfeld = [0] * dimension

            for x_position in range(dimension):
                self.__spielfeld[x_position] = [0] * dimension

    @property
    def spielfeld(self):
        """Getter fuer Spielfeld

        Returns:
            int[][]: Spielfeld
        """
        return self.__spielfeld

    @spielfeld.setter
    def spielfeld(self, spielfeld):
        self.__spielfeld = spielfeld

    def set_feld(self, staus: int, koordinaten: Koordinaten):
        """Setzt den Satus eines bestimmten Feldes

        Args:
            staus (int): -1 =daneben, 0 = neutral, 1 = treffer, 2 = Schiff
            koordinaten (Koordinaten): Position
        """
        self.__spielfeld[koordinaten.x][koordinaten.y] = staus

    def plaziere_schiff(self, koordinaten: Koordinaten, richtung: int, schiff: Schiff):
        """
        Plaziert das Schaff auf der Angegebenen Position in die entsprechende Richtung

        Args:
            koordinaten (Koordinaten): Startpunkt
            richtung (int): 0-Norden, 1-Osten, 2-Sueden, 3-Westen
            schiff (Schiff): Das zu plazierende Schiff
        """
        # Ermittle alle Koordinaten wo das Schiff sein wird
        koordinaten_schiff_alle = self.__get_koordinaten_in_richtung(koordinaten, richtung, schiff.groesse)

        if len(koordinaten_schiff_alle) != schiff.groesse:
            raise IndexError(f"Das Schiff kann so nicht plaziert werden! Start:{koordinaten.x},{koordinaten.y} Richtung:{richtung}")

        # Checke ob das Schiff platziert werden darf
        for koordinaten_schiff in koordinaten_schiff_alle:
            if not self.__valides_plazieren(koordinaten_schiff):
                raise IndexError(f"Das Schiff kann so nicht plaziert werden! Start:{koordinaten.x},{koordinaten.y} Richtung:{richtung}")

        # Plaziere Schiff
        for koordinaten_schiff in koordinaten_schiff_alle:
            self.set_feld(2, koordinaten_schiff)

    def get_status_bei(self, koordinaten: Koordinaten) -> int:
        """
        Gibt den Status des Feldes an der entsprechenden Position zurueck

        Args:
            koordinaten (Koordinaten): Position welche ueberprueft wird

        Returns:
            int: -1 daneben, 0 neutral/Wasser, 1 treffer, 2 Schiff
        """
        return self.__spielfeld[koordinaten.x][koordinaten.y]

    def alle_schiffe_zerstoert(self) -> bool:
        """Zum uberpruefen ob ein Spieler verloren hat, bzw ob noch ein intaktes Schiffteil
        auf dem Spielfeld vorhanden ist

        Returns:
            Boolean: True - Kein Schiffsteil mehr uebrig, False - Mindestens ein Teil uebrig
        """
        for x_felder in self.__spielfeld:
            for feld in x_felder:
                if feld != 0:
                    return False

        return True

    def reset(self):
        """Setzt alle Felder auf den Wert 0
        """
        for x_felder in self.__spielfeld:
            for feld in x_felder:
                feld = 0

    def __valides_plazieren(self, koordinaten: Koordinaten) -> bool:
        """Checkt alle Felder um der entsprechendenKoordinate und schaut, ob dort ein Schiff plaziert ist

        Args:
            koordinaten (Koordinaten): Position

        Returns:
            bool: True - nur Wasser, False - nicht nur Wasser
        """
        alle_koordinaten = self.__get_koordinaten_drumherum(koordinaten)

        for valide_koordinaten in alle_koordinaten:
            tmp_status = self.get_status_bei(valide_koordinaten)
            if tmp_status != 0:
                return False

        return True

    def __get_koordinaten_drumherum(self, koordinaten: Koordinaten) -> list:
        """Gibt alle moeglichen Koordinaten um eine entsprechende Position inklusive die uebergebene Position selbst

        Args:
            koordinaten (Koordinaten): Position

        Returns:
            list: Mit allen validen Koordinaten
        """

        gueltige_koordinaten = []

        try:
            x_start_position = koordinaten.x-1
            y_start_position = koordinaten.y-1

            for x_position in range(3):
                for y_position in range(3):

                    tmp_koordinaten = Koordinaten(x_start_position+x_position, y_start_position+y_position)
                    gueltige_koordinaten.append(tmp_koordinaten)

        except IndexError:
            # Out of Range wird nicht beachtet
            pass

        return gueltige_koordinaten

    def __get_koordinaten_in_richtung(self, koordinaten: Koordinaten, richtung: int, anzahl_felder: int) -> list:
        """Gibt die Koordinaten an, in welcher sich ein Schiff theoretisch befinden wird

        Args:
            koordinaten (Koordinaten): Start Position
            richtung (int): 0-Norden, 1-Osten, 2-Sueden, 3-Westen
            anzahl_felder (int): wie weit in die Richtung gegangen wird

        Returns:
            list: Alle Koordinaten
        """
        koordinaten_schiff = []

        # Norden
        if richtung == 0:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinaten.x + y_position_counter
                y_position = koordinaten.y

                tmp_koordinaten = Koordinaten(x_position, y_position)
                koordinaten_schiff.append(tmp_koordinaten)

        # Osten
        elif richtung == 1:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinaten.x
                y_position = koordinaten.y + y_position_counter

                tmp_koordinaten = Koordinaten(x_position, y_position)
                koordinaten_schiff.append(tmp_koordinaten)

        # Sueden
        elif richtung == 2:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinaten.x - y_position_counter
                y_position = koordinaten.y

                tmp_koordinaten = Koordinaten(x_position, y_position)
                koordinaten_schiff.append(tmp_koordinaten)

        # Westen
        elif richtung == 3:
            for y_position_counter in range(anzahl_felder):

                x_position = koordinaten.x
                y_position = koordinaten.y - y_position_counter

                tmp_koordinaten = Koordinaten(x_position, y_position)
                koordinaten_schiff.append(tmp_koordinaten)

        return koordinaten_schiff
