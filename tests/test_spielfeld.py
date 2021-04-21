import unittest
import random

from schiffeversenken.spielfeld import Spielfeld
from schiffeversenken.koordinate import Koordinate
from schiffeversenken.schiff import Schiff
from schiffeversenken import Status, Richtung


class Test_Spielfeld(unittest.TestCase):

    # So in bildlich richtig
    # 0/0, 1/0, 2/0, 3/0, 4/0,
    # 0/1, 1/1, 2/1, 3/1, 4/1,
    # 0/2, 1/2, 2/2, 3/2, 4/2,
    # 0/3, 1/3, 2/3, 3/3, 4/3,
    # 0/4, 1/4, 2/4, 3/4, 4/4,
    # 0/5, 1/5, 2/5, 3/5, 4/5,
    # 0/6, 1/6, 2/6, 3/6, 4/6,
    # 0/7, 1/7, 2/7, 3/7, 4/7,
    # 0/8, 1/8, 2/8, 3/8, 4/8,
    # 0/9, 1/9, 2/9, 3/9, 4/9,

    # so muss man es erstellen
    # >>> pprint(m)
    # [['0/0', '0/1', '0/2', '0/3', '0/4', '0/5', '0/6', '0/7', '0/8', '0/9'],
    #  ['1/0', '1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9'],
    #  ['2/0', '2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9'],
    #  ['3/0', '3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9'],
    #  ['4/0', '4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9'],
    #  ['5/0', '5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9'],
    #  ['6/0', '6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9'],
    #  ['7/0', '7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9'],
    #  ['8/0', '8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9'],
    #  ['9/0', '9/1', '9/2', '9/3', '9/4', '9/5', '9/6', '9/7', '9/8', '9/9']]

    def setUp(self):
        self.leeres_spielfeld = [[Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]

        self.befuelltes_spielfeld = [[Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.TREFFER, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.SCHIFF, Status.TREFFER, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]

        self.kurzes_spielfeld = [[Status.WASSER, Status.WASSER],
                                 [Status.WASSER, Status.WASSER]]

    def test_konstruktoren(self):
        leeres_spielfeld_obj = Spielfeld()
        geladenes_spielfeld_obj = Spielfeld(spielfeld=self.befuelltes_spielfeld)
        kurzes_spielfeld_obj = Spielfeld(dimension=2)

        self.assertEqual(leeres_spielfeld_obj.spielfeld, self.leeres_spielfeld)
        self.assertEqual(geladenes_spielfeld_obj.spielfeld, self.befuelltes_spielfeld)
        self.assertEqual(kurzes_spielfeld_obj.spielfeld, self.kurzes_spielfeld)

    def test_setter_getter(self):
        spielfeld_obj = Spielfeld()

        self.assertEqual(spielfeld_obj.spielfeld, self.leeres_spielfeld)

        spielfeld_obj.spielfeld = self.befuelltes_spielfeld
        get_spielfeld = spielfeld_obj.spielfeld

        self.assertEqual(get_spielfeld, self.befuelltes_spielfeld)
        self.assertNotEqual(get_spielfeld, self.leeres_spielfeld)

    def test_set_feld(self):
        spielfeld_obj = Spielfeld()
        statusse = list(Status)

        for y in range(1, 11):
            for x in range(1, 11):
                status = random.choice(statusse)
                position = Koordinate(x, y)
                spielfeld_obj.set_feld(status, position)
                self.assertEqual(spielfeld_obj.spielfeld[x-1][y-1], status)

    def test_plaziere_schiff(self):

        spielfeld_obj = Spielfeld()
        schiff = Schiff("U-Boot", 2)

        spielfeld_mit_plaziertem_schiff_sueden = [[Status.SCHIFF, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                  [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]

        spielfeld_mit_plaziertem_schiff_osten = [[Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                                 [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]

        koordinate = Koordinate(1, 1, Richtung.SUEDEN)  # index [0][0] sueden
        spielfeld_obj.plaziere_schiff(koordinate, schiff)
        self.assertEqual(spielfeld_obj.spielfeld, spielfeld_mit_plaziertem_schiff_sueden)

        spielfeld_obj.reset()

        koordinate = Koordinate(1, 1, Richtung.OSTEN)  # index [0][0] osten
        spielfeld_obj.plaziere_schiff(koordinate, schiff)
        self.assertEqual(spielfeld_obj.spielfeld, spielfeld_mit_plaziertem_schiff_osten)

        spielfeld_obj.reset()

        koordinate = Koordinate(1, 1, Richtung.NORDEN)  # index [0][0] norden
        self.assertRaises(IndexError, spielfeld_obj.plaziere_schiff, koordinate, schiff)

        koordinate = Koordinate(1, 1, Richtung.WESTEN)  # index [0][0] westen
        self.assertRaises(IndexError, spielfeld_obj.plaziere_schiff, koordinate, schiff)

        koordinate = Koordinate(12, 1, Richtung.NORDEN)  # index fehlerhaft
        self.assertRaises(IndexError, spielfeld_obj.plaziere_schiff, koordinate, schiff)
        
        koordinate = Koordinate("Z", 1, Richtung.NORDEN)  # index fehlerhaft
        self.assertRaises(IndexError, spielfeld_obj.plaziere_schiff, koordinate, schiff)

        spielfeld_obj_befuellt = Spielfeld(spielfeld=self.befuelltes_spielfeld)
        koordinate_befuellt = Koordinate(4, 8, Richtung.NORDEN)  # index[3][7] norden

        self.assertRaises(IndexError, spielfeld_obj_befuellt.plaziere_schiff, koordinate_befuellt, schiff)

    def test_get_status_bei(self):
        spielfeld_obj = Spielfeld()
        statusse = list(Status)

        for y in range(1, 11):
            for x in range(1, 11):
                koordinate = Koordinate(x, y)

                status = random.choice(statusse)

                spielfeld_obj.spielfeld[x-1][y-1] = status
                spielfeld_status = spielfeld_obj.get_status_bei(koordinate)

                self.assertEqual(status, spielfeld_status)

    def test_alle_schiffe_zerstoert(self):
        befuelltes_spielfeld_obj = Spielfeld(spielfeld=self.befuelltes_spielfeld)
        leeres_spielfeld_obj = Spielfeld()

        self.assertEqual(befuelltes_spielfeld_obj.alle_schiffe_zerstoert(), False)
        self.assertEqual(leeres_spielfeld_obj.alle_schiffe_zerstoert(), True)

    def test_reset(self):
        geladenes_spielfeld_obj = Spielfeld(spielfeld=self.befuelltes_spielfeld)
        geladenes_spielfeld_obj.reset()

        self.assertEqual(geladenes_spielfeld_obj.spielfeld, self.leeres_spielfeld)
