import datetime
from enum import Enum, unique
from datetime import datetime


@unique
class Status(Enum):
    DANEBEN = -1
    WASSER = 0
    TREFFER = 1
    SCHIFF = 2
    UNGUELTIG = 3

@unique
class Farben(Enum):
    GRUEN = "\033[0;32m"
    FARB_ENDE = "\033[0m"


@unique
class Richtung(Enum):
    NORDEN = 0
    OSTEN = 1
    SUEDEN = 2
    WESTEN = 3


class Rahmenzeichen(Enum):
    HEAVY_VERTICAL = "\u2503"
    #TODO Weitere Zeichen einfuegen

class Speicherverwaltung():

    def speichern(self, pfad:str=f"{datetime.now().day}_{datetime.now().month}_{datetime.now().year}.json"):
        print(pfad)

    def laden(self, pfad:str)->dict:
        pass

#TODO Speichern und Lesen erstellen