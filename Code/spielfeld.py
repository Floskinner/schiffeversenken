"""[summary]
"""

from koordinaten import Koordinaten
from schiff import Schiff


class Spielfeld():
    """[summary]
    """

    def __init__(self, *args):
        """Erstelle Spielfeld
        args = 0 -> Standartspiellaenge von 10 mal 10 wird erstellt
        args = 1 -> Spielfeld: int[][] fetiges Spielfeld wird übernommen
        args = 2 -> X: int, Y: int Spielfeld von X mal Y wird erstellt
        """

        x_laenge = 10
        y_laenge = 10
        self.__spielfeld: int = [[]]

        anzahl_argumente = len(args)

        if anzahl_argumente == 1:
            self.spielfeld = args[0]

        else:
            if anzahl_argumente == 2:
                x_laenge = args[0]
                y_laenge = args[1]

            self.__spielfeld = [0] * x_laenge

            for x_position in range(x_laenge):
                self.__spielfeld[x_position] = [0] * y_laenge

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

    def plaziere_schiff(self, koordinaten: Koordinaten, richtung: int, schiff: Schiff):
        """
        Plaziert das Schaff auf der Angegebenen Position in die entsprechende Richtung

        Args:
            koordinaten (Koordinaten): Startpunkt
            richtung (int): 0-Norden, 1-Osten, 2-Sueden, 3-Westen
            schiff (Schiff): Das zu plazierende Schiff
        """
        pass

    def get_status_bei(self, koordinaten: Koordinaten) -> int:
        """
        Gibt den Status des Feldes an der entsprechenden Position zurueck

        Args:
            koordinaten (Koordinaten): Position welche ueberprueft wird

        Returns:
            int: -1 daneben, 0 neutral/Wasser, 1 treffer, 2 Schiff
        """
        pass

    def alle_schiffe_zerstoert(self) -> bool:
        """Zum uberpruefen ob ein Spieler verloren hat, bzw ob noch ein intaktes Schiffteil
        auf dem Spielfeld vorhanden ist

        Returns:
            Boolean: True - Kein Schiffsteil mehr uebrig, False - Mindestens ein Teil uebrig
        """
        pass

    def reset(self):
        """Setzt alle Felder auf den Wert 0
        """
        pass

    def __valides_plazieren(self, koordinaten: Koordinaten) -> bool:
        """Checkt alle Felder um der entsprechendenKoordinate und schaut, ob dort ein Schiff plaziert ist

        Args:
            koordinaten (Koordinaten): Position

        Returns:
            bool: True - nur Wasser, False - nicht nur Wasser
        """
        pass

    def __get_koordinaten_drumherum(self, koordinaten: Koordinaten) -> Koordinaten:
        """Gibt alle moeglichen Koordinaten um eine entsprechende Position

        Args:
            koordinaten (Koordinaten): Position

        Returns:
            Koordinaten[]: Array mit allen validen Koordinaten
        """
        pass
