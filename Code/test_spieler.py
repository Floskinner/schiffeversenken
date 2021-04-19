import unittest
import random

from spielfeld import Spielfeld
from koordinate import Koordinate
from schiff import Schiff
from spieler import Spieler
from helferklasse import Status, Richtung


class Test_Spieler(unittest.TestCase):

    def test_konstruktoren(self):
        name = "Name"
        spielfeld = Spielfeld()
        spielfeld_gegner = Spielfeld()
        punkte = 200

        spieler = Spieler(name, spielfeld, spielfeld_gegner, punkte)

        self.assertEqual(spieler.name, name)
        self.assertEqual(spieler.spielfeld, spielfeld)
        self.assertEqual(spieler.spielfeld_gegner, spielfeld_gegner)
        self.assertEqual(spieler.punkte, punkte)

    def test_update_spielfeld_gegner(self):

        statusse = list(Status)
        test_spieler = Spieler("TestName", Spielfeld(), Spielfeld(), 0)

        for y in range(1, 11):
            for x in range(1, 11):
                koordinate = Koordinate(x, y)
                status = random.choice(statusse)

                test_spieler.update_spielfeld_gegner(koordinate, status)
                status_spielfeld = test_spieler.spielfeld_gegner.get_status_bei(koordinate)

                self.assertEqual(status, status_spielfeld)

    def test_update_spielfeld(self):
        statusse = list(Status)
        test_spieler = Spieler("TestName", Spielfeld(), Spielfeld(), 0)

        for y in range(1, 11):
            for x in range(1, 11):
                koordinate = Koordinate(x, y)
                status = random.choice(statusse)

                test_spieler.update_spielfeld(koordinate, status)
                status_spielfeld = test_spieler.spielfeld.get_status_bei(koordinate)

                self.assertEqual(status, status_spielfeld)


    def test_add_punkt(self):
        punkt_add = 10
        test_spieler = Spieler("TestName", Spielfeld(), Spielfeld(), 0)

        aktuelle_punkte = test_spieler.punkte
        test_spieler.add_punkt()

        self.assertEqual(aktuelle_punkte+1 , test_spieler.punkte)

        aktuelle_punkte = test_spieler.punkte
        test_spieler.add_punkt(punkt_add)

        self.assertEqual(aktuelle_punkte+punkt_add , test_spieler.punkte)

    
    def test_wird_abgeschossen(self):
        statusse = list(Status)
        test_spieler = Spieler("TestName", Spielfeld(), Spielfeld(), 0)

        for y in range(1, 11):
            for x in range(1, 11):
                koordinate = Koordinate(x, y)
                status = random.choice(statusse)

                test_spieler.update_spielfeld(koordinate, status)
                
                if status == Status.SCHIFF:
                    return_schuss = test_spieler.wird_abgeschossen(koordinate)

                    self.assertEqual(return_schuss, Status.TREFFER)

                else:
                    return_schuss = test_spieler.wird_abgeschossen(koordinate)

                    self.assertEqual(return_schuss, status)


    def test_is_tot(self):
        test_spieler = Spieler("TestName", Spielfeld(), Spielfeld(), 0)

        #Spielfeld von vorne rein Leer - somit kein Schiff mehr vorhanden -> tot
        self.assertEqual(test_spieler.is_tot(), True)

        test_spieler.update_spielfeld(Koordinate(1,1), Status.SCHIFF)

        self.assertEqual(test_spieler.is_tot(), False)