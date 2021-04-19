"""Das Modul enthaelt diverse Helferklassen / Enums / Funktionen die Global hilfreich sind
"""

import datetime
import json
from enum import IntEnum, Enum, unique
from datetime import datetime
from typing import Union, Optional


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
    # TODO Weitere Zeichen einfuegen


def user_input(text: str, datentyp: Union[str, int], erlaubte_werte: Optional[Union[list[str], list[int]]] = None) -> Union[str, int]:
    """Der User wird so lange gezwungen einen Richtige eingabe machen, bis alle Kritieren (type, erlaubte_werte) erfuellt sind

    Args:
        text (str): Text welches dem input() uebergeben wird
        datentyp (Union[str, int]): Festelgen ob ein str oder int zurueckgegeben werden soll
        erlaubte_werte (Optional[Union[list[str], list[int]]], optional): Liste aus str oder int, die eigegebenen Werte muessen in der
                                                                          Liste enthalten sein, sonst ist die Eingabe ungueltig. Defaults to None.

    Raises:
        ValueError: Wird erzeugt, wenn die Usereingabe falsch war. Wird jedoch intern abgefangen!

    Returns:
        Union[str, int]: Entsprechender valide Usereingabe
    """
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
    """Speichert die Daten entsprechend dem Pfad als json ab

    Args:
        daten (dict): Daten welche gespeichert werden
        pfad (str, optional): Speicherpfad. Defaults to f"{datetime.now().day}_{datetime.now().month}_{datetime.now().year}.json".
    """
    with open(pfad, 'w') as outfile:
        json.dump(daten, outfile)


def laden(pfad: str) -> dict:
    """Ladet einen entprechende json Datei

    Args:
        pfad (str): Pfad zur json

    Returns:
        dict: umgewandelte json
    """
    with open(pfad) as json_file:
        daten = json.load(json_file)

    return daten
