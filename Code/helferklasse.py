import datetime
import json
from enum import IntEnum, Enum, unique
from datetime import datetime
from typing import Union, Optional


@unique
class Status(IntEnum):
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
    # TODO Weitere Zeichen einfuegen


def user_input(text: str, datentyp: Union[str, int], erlaubte_werte: Optional[Union[list[str], list[int]]] = None) -> Union[str, int]:
    ist_valide = False
    data: datentyp

    while not ist_valide:
        try:
            data = input(text).strip()

            if isinstance(datentyp, int):
                data = int(data)

            if erlaubte_werte is not None:
                if data not in erlaubte_werte:
                    raise ValueError

            ist_valide = True
        except ValueError:
            print("Ungueltige Eingabe!")

    return data


def speichern(daten: dict, pfad: str = f"{datetime.now().day}_{datetime.now().month}_{datetime.now().year}.json"):
    with open(pfad, 'w') as outfile:
        json.dump(daten, outfile)

def laden(pfad: str) -> dict:
    with open(pfad) as json_file:
        daten = json.load(json_file)

    return daten
