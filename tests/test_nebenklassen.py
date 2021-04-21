import unittest

from io import StringIO
from unittest.mock import patch

from schiffeversenken import Richtung
from schiffeversenken.koordinate import Koordinate
from schiffeversenken.schiff import Schiff
import schiffeversenken.helferklasse as helferklasse


class Test_Nebenklassen(unittest.TestCase):

    def test_schiff(self):
        name = "Zerstoerer"
        groesse = 5
        schiff = Schiff(name, groesse)

        self.assertEqual(schiff.name, name)
        self.assertEqual(schiff.groeße, groesse)

    def test_koordinaten(self):
        x_A = "A"
        x_1 = 1

        y_A = "A"
        y_1 = 1

        koordinate_x_string = Koordinate(x_A, y_1)
        koordinate_x_int = Koordinate(x_1, y_1)
        koordinate_y_string = Koordinate(x_1, y_A)
        koordinate_x_y_string = Koordinate(x_A, y_A)

        self.assertEqual(koordinate_x_string.x_position, 0)
        self.assertEqual(koordinate_x_string.y_position, 0)

        self.assertEqual(koordinate_x_int.x_position, 0)
        self.assertEqual(koordinate_x_int.y_position, 0)

        self.assertEqual(koordinate_y_string.x_position, 0)
        self.assertEqual(koordinate_y_string.y_position, 0)

        self.assertEqual(koordinate_x_y_string.x_position, 0)
        self.assertEqual(koordinate_x_y_string.y_position, 0)

        koordinate_mit_richtung = Koordinate(x_1, y_1, Richtung.NORDEN)
        self.assertEqual(koordinate_mit_richtung.richtung, Richtung.NORDEN)

        koordinate_mit_richtung.richtung = Richtung.SUEDEN
        self.assertEqual(koordinate_mit_richtung.richtung, Richtung.SUEDEN)

    def test_user_input(self):

        inputs_int_gut = (1, 2, 3, 4)
        inputs_int_valide = (1, 2, 3, 4)

        for expected_input in inputs_int_gut:

            with patch('sys.stdin', new=StringIO(str(expected_input))):
                value = helferklasse.user_input("Eingabe: ", int(), inputs_int_valide)
                self.assertTrue(isinstance(value, int))
                self.assertEqual(value, expected_input)

        inputs_str_gut = ("1", "2", "3", "4")
        inputs_str_valide = ("1", "2", "3", "4")

        for expected_input in inputs_str_gut:

            with patch('sys.stdin', new=StringIO(str(expected_input))):
                value = helferklasse.user_input("Eingabe: ", str, inputs_str_valide)
                self.assertTrue(isinstance(value, str))
                self.assertEqual(value, expected_input)

    # TODO Testen von Speichern und Lesen
