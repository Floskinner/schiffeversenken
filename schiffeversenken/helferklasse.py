"""Das Modul enthaelt diverse Helferklassen / Enums / Funktionen die Global hilfreich sind
"""

import datetime
import json

from datetime import datetime
from typing import Union, Optional

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
