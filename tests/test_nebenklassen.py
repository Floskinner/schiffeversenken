import unittest

from io import StringIO
from unittest.mock import patch

import schiffeversenken.helferklasse as helferklasse
from schiffeversenken.koordinate import Koordinate
from schiffeversenken.schiff import Schiff


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
        
        y_1 = 1

        koordinate = Koordinate(x_A, y_1)
        koordinate_2 = Koordinate(x_1, y_1)

        self.assertEqual(koordinate.x_position, 0)
        self.assertEqual(koordinate.y_position, 0)
        
        self.assertEqual(koordinate_2.x_position, 0)
        self.assertEqual(koordinate_2.y_position, 0)

    def test_user_input(self):

        inputs_int_gut = (1, 2, 3, 4)
        inputs_int_valide = (1, 2, 3, 4)

        for expected_input in inputs_int_gut:

            with patch('sys.stdin', new=StringIO(str(expected_input))):
                value = helferklasse.user_input("Eingabe: ", int(), inputs_int_valide)
                self.assertTrue(isinstance(value, int))
                self.assertEquals(value, expected_input)

        inputs_str_gut = ("1", "2", "3", "4")
        inputs_str_valide = ("1", "2", "3", "4")

        for expected_input in inputs_str_gut:

            with patch('sys.stdin', new=StringIO(str(expected_input))):
                value = helferklasse.user_input("Eingabe: ", str, inputs_str_valide)
                self.assertTrue(isinstance(value, str))
                self.assertEquals(value, expected_input)
        

    #TODO Testen von Speichern und Lesen
