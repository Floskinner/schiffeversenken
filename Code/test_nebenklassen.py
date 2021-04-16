import unittest
from koordinate import Koordinate
from schiff import Schiff


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

    #TODO Testen von Speichern und Lesen
