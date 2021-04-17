from spieler import Spieler
import unittest
from spielfeld import Spielfeld
from koordinate import Koordinate
from schiff import Schiff
from master import Master
from helferklasse import Status
from io import StringIO
from unittest.mock import patch


class Test_Master(unittest.TestCase):

    
    
    def setUp(self) -> None:
        self.master = Master()
        self.befuelltes_spielfeld_list = [[Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.TREFFER, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.SCHIFF, Status.TREFFER, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.WASSER],
                                     [Status.DANEBEN, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.SCHIFF, Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]

        self.befuelltes_spielfeld = Spielfeld(spielfeld=self.befuelltes_spielfeld_list)
        self.spieler_1 = Spieler("Test1", self.befuelltes_spielfeld, Spielfeld(),0)
        self.master.aktueller_spieler = self.spieler_1
        self.master.spieler_1 = self.spieler_1      
        self.spieler_2 = Spieler("Test2", self.befuelltes_spielfeld, Spielfeld(), 0)
        self.master.spieler_2 = self.spieler_2
        self.master.aktueller_gegner = self.spieler_2
        self.test_koordinate_treffer = Koordinate('A',1)
        self.test_koordinate_daneben = Koordinate('E',1)
        return super().setUp()

    def test_print_spielfeld(self):            
        self.master.print_spielfeld(self.spieler_1.spielfeld)

    def test_schiessen(self):
        status:Status = self.master.schiessen(self.spieler_1, self.spieler_2, self.test_koordinate_treffer)
        self.assertEqual(Status.TREFFER, status)
        self.assertNotEqual(Status.DANEBEN, status)
        status:Status = self.master.schiessen(self.spieler_1, self.spieler_2, self.test_koordinate_daneben)
        self.assertEqual(Status.DANEBEN, status)
        self.assertNotEqual(Status.TREFFER, status)

    def test_spielen(self):
        self.master.spielen()

    def test_toggle_spielzug(self):
        self.master.toggle_spielzug()
        self.assertEqual(self.spieler_2, self.master.aktueller_spieler)

    def test_print_rahmen_oben(self):
        expected_output = "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_rahmen_oben()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_rahmen_unten(self):
        expected_output = "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_rahmen_unten()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_trennlinie(self):
        expected_output = "┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_trennlinie()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_get_spieler_1(self):
        spieler = self.master.spieler_1
        self.assertEqual(self.spieler_1, self.master.spieler_1)

    def test_get_spieler_2(self):
        spieler = self.master.spieler_2
        self.assertEqual(self.spieler_2, self.master.spieler_2)

if __name__ == '__main__':
    unittest.main()
