from spieler import Spieler
import unittest
from spielfeld import Spielfeld
from koordinate import Koordinate
from schiff import Schiff
from master import Master
from helferklasse import Richtung, Status
from io import StringIO
from unittest.mock import patch
from pynput import keyboard


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
        self.test_get_user_input_koordinate = Koordinate('A',10)
        self.test_ungueltige_koordinate = Koordinate('A',12)
        self.test_koordinate_treffer = Koordinate('A',1)
        self.test_koordinate_daneben = Koordinate('E',1)
        return super().setUp()

    def test_print_spielfeld(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_spielfeld(self.spieler_1.spielfeld)
            count_schiffe = fake_out.getvalue().count('#')
            count_daneben = fake_out.getvalue().count('O')
            count_treffer = fake_out.getvalue().count('X')
            count_A = fake_out.getvalue().count('A')
            count_B = fake_out.getvalue().count('B')
            count_C = fake_out.getvalue().count('C')
            count_D = fake_out.getvalue().count('D')
            count_E = fake_out.getvalue().count('E')
            count_F = fake_out.getvalue().count('F')
            count_G = fake_out.getvalue().count('G')
            count_H = fake_out.getvalue().count('H')
            count_I = fake_out.getvalue().count('I')
            count_J = fake_out.getvalue().count('J')
            self.assertEqual(count_schiffe, 13)
            self.assertEqual(count_treffer, 2)
            self.assertEqual(count_daneben, 1)
            self.assertEqual(count_A,1)
            self.assertEqual(count_B,1)
            self.assertEqual(count_C,1)
            self.assertEqual(count_D,1)
            self.assertEqual(count_E,1)
            self.assertEqual(count_F,1)
            self.assertEqual(count_G,1)
            self.assertEqual(count_H,1)
            self.assertEqual(count_I,1)
            self.assertEqual(count_J,1)
            

    def test_get_user_input(self):
        expected_input = "A10"
        with patch('sys.stdin', new=StringIO(expected_input)):
            got_input:Koordinate = self.master.get_user_input_koordinate()
            self.assertEqual(got_input.x_position, self.test_get_user_input_koordinate.x_position)
            self.assertEqual(got_input.y_position, self.test_get_user_input_koordinate.y_position)

    def test_schiessen_mit_gueltiger_koordinate(self):
        status:Status = self.master.schiessen(self.spieler_1, self.spieler_2, self.test_koordinate_treffer)
        self.assertEqual(Status.TREFFER, status)
        self.assertNotEqual(Status.DANEBEN, status)
        status:Status = self.master.schiessen(self.spieler_1, self.spieler_2, self.test_koordinate_daneben)
        self.assertEqual(Status.DANEBEN, status)
        self.assertNotEqual(Status.TREFFER, status)

    def test_schiessen_mit_ungueltiger_koordinate(self):
        status:Status = self.master.schiessen(self.spieler_1, self.spieler_2, self.test_ungueltige_koordinate)
        self.assertEqual(Status.UNGUELTIG, status)

    def test_platziere_schiffe(self):
        spielfeld:Spielfeld = self.master.platziere_schiff(self.master.aktueller_spieler.name, Spielfeld(), Schiff("Schlachtschiff", 5), 
        Koordinate("A",1), Richtung.SUEDEN)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_spielfeld(spielfeld)
            count_schiffe = fake_out.getvalue().count('#')
            self.assertEqual(count_schiffe, 5)

    def test_esc_gedrueckt(self):
        self.master.esc_gedrueckt(keyboard.Key.esc)
        self.assertEqual(self.master.speichern_flag, True)


    def test_print_alles_fuer_spielzug(self):
        self.master.print_alles_fuer_spielzug()

    def test_spielen(self):
        #self.master.spielen()
        pass

    def test_toggle_spielzug(self):
        self.master.toggle_spielzug()
        self.assertEqual(self.spieler_2, self.master.aktueller_spieler)

    # def test_print_rahmen_oben(self):
    #     expected_output = "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.master.__print_rahmen_oben()
    #         self.assertEqual(fake_out.getvalue(), expected_output)

    # def test_print_rahmen_unten(self):
    #     expected_output = "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n"
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.master.__print_rahmen_unten()
    #         self.assertEqual(fake_out.getvalue(), expected_output)

    # def test_print_trennlinie(self):
    #     expected_output = "┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃\n"
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.master.__print_trennlinie()
    #         self.assertEqual(fake_out.getvalue(), expected_output)

    def test_get_spieler_1(self):
        spieler = self.master.spieler_1
        self.assertEqual(self.spieler_1, self.master.spieler_1)

    def test_get_speichern_flag_bei_spielbeginn(self):
        expected_speicher_flag = False
        master = Master()
        speichern_flag = master.speichern_flag
        self.assertEqual(speichern_flag, expected_speicher_flag)

    def test_get_speichern_flag_nach_esc_gedrueckt(self):
        expected_speicher_flag = True
        master = Master()
        master.esc_gedrueckt(keyboard.Key.esc)
        speichern_flag = master.speichern_flag
        self.assertEqual(speichern_flag, expected_speicher_flag)

    def test_get_spieler_2(self):
        spieler = self.master.spieler_2
        self.assertEqual(self.spieler_2, self.master.spieler_2)

if __name__ == '__main__':
    unittest.main()
