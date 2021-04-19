"""Modul, welches die Klasse Koordinate beinhaltet"""
from helferklasse import Richtung
from typing import Union, Optional

class Koordinate:
    """Speichert einen X und Y Wert. Beim erstellen des Objektes wird direkt 1 abgezogen, damit
    die gespeicherten X und Y Werte direkt einem Array-Index zugeordnet werden koennen
    """

    def __init__(self, x_wert: Union[int, str], y_wert: Union[int, str], richtung:Optional[Richtung] = None):
        """Usereingaben werden als Array freundliche Werte gespeichert mit Optionaler Richtung

        Args:
            x_wert (Union[int, str]): X Position, A bis Z wird entsprechend Umngeadnelt A = index 0
            y_wert (int): X Position, A bis Z wird entsprechend Umngeadnelt A = index 0
            richtung (Optional[Richtung]): Kann eine entsprechende Richtung mit uebergeben werden. Defaults to None.
        """

        if isinstance(x_wert, str):
            x_wert = self.__umwandeln_in_int(x_wert)
        if isinstance(y_wert, str):
            y_wert = self.__umwandeln_in_int(y_wert)

        self.__x_position = x_wert - 1
        self.__y_position = y_wert - 1
        self.__richtung = richtung

    @property
    def x_position(self) -> int:
        """Gibt entsprechenden X-Wer der Koordinate zurueck

        Returns:
            int: X-Wert
        """
        return self.__x_position

    @property
    def y_position(self) -> int:
        """Gibt entsprechenden Y-Wer der Koordinate zurueck

        Returns:
            int: Y-Wert
        """
        return self.__y_position

    @property
    def richtung(self) -> Richtung:
        """Gibt die Richtung an

        Returns:
            Richtung: Norden, Sueden, Westen, Osten
        """
        return self.__richtung

    def __umwandeln_in_int(self, buchstabe: str) -> int:
        """Wandelt Buchsten in den Entsprechenden Index um, wobei A = 1, B = 2, C = 3... entspricht
        Anders gesagt, die Position des Buchstaben im Alphabet

        Args:
            buchstabe (str): Groß- oder Kleinbuchstabe

        Returns:
            int: Position im Alphabet
        """
        buchstabe = buchstabe.upper()
        index = ord(buchstabe) - 64  # A wird zu 1, B zu 2...
        return index
