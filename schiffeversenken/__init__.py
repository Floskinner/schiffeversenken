"""Startet ein volles Schiffeversenken Spiel
"""

from enum import IntEnum, Enum, unique
from schiffeversenken.schiff import Schiff

__schiffe__: list = [Schiff("Schlachtschiff", 5),
                    Schiff("Kreuzer", 4), Schiff("Kreuzer", 4),
                    Schiff("Zerstoerer", 3), Schiff("Zerstoerer", 3), Schiff("Zerstoerer", 3),
                    Schiff("U-Boot", 2), Schiff("U-Boot", 2), Schiff("U-Boot", 2), Schiff("U-Boot", 2)]

@unique
class Status(IntEnum):
    """IntEnum fuer das Spielfeld
    """
    DANEBEN = -1
    WASSER = 0
    TREFFER = 1
    SCHIFF = 2
    UNGUELTIG = 3


@unique
class Farben(Enum):
    """Enum fuer verschiedene Terminalfarben
    """
    GRUEN = "\033[0;32m"
    ROT = "\033[31m"
    BLAU = "\033[34m"
    FARB_ENDE = "\033[0m"


@unique
class Richtung(Enum):
    """Enum fuer verschiedene Himmelsrichtungen
    """
    NORDEN = 0
    OSTEN = 1
    SUEDEN = 2
    WESTEN = 3


class Rahmenzeichen(Enum):
    """Enum um die Sonderzeichen besser zu ordnen
    """
    HEAVY_VERTICAL = "\u2503"
    HEAVY_HORIZONTAL = "\u2501"
