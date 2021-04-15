from enum import Enum

class Status(Enum):
    DANEBEN = -1
    WASSER = 0
    TREFFER = 1
    SCHIFF = 2

class Richtung(Enum):
    NORDEN = 0
    OSTEN = 1
    SUEDEN = 2
    WESTEN = 3

class Rahmenzeichen(Enum):
    HEAVY_VERTICAL = "\u2503"



