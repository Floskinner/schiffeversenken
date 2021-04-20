"""Modul welches die Klasse Schiff enthalet"""
class Schiff():
    """Hiermit kann ein Schiff mit einer entsprechenden Laenge erstellt werden
    """

    def __init__(self, name: str, groeße: int):
        self.__name: str = name
        self.__groeße: int = groeße

    @property
    def name(self) -> str:
        """Gibt entsprechenden Namen vom Schiff zurueck

        Returns:
            str: Name
        """
        return self.__name

    @property
    def groeße(self) -> int:
        """Gibt entsprechenden Namen vom Schiff zurueck

        Returns:
            int: Name
        """
        return self.__groeße
