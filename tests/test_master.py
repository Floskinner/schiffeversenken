#pylint: disable=c

import os
import platform
import unittest

from unittest.mock import patch
from io import StringIO

from schiffeversenken.spieler import Spieler
from schiffeversenken.spielfeld import Spielfeld
from schiffeversenken.koordinate import Koordinate
from schiffeversenken.schiff import Schiff
from schiffeversenken.master import Master
from schiffeversenken import Richtung, Status


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

        self.befuelltes_spielfeld_letzter_schuss_list = [[Status.SCHIFF, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER],
                                     [Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER, Status.WASSER]]                             

        self.befuelltes_spielfeld = Spielfeld(spielfeld=self.befuelltes_spielfeld_list)
        self.befuelltes_spielfeld_letzter_schuss = Spielfeld(spielfeld = self.befuelltes_spielfeld_letzter_schuss_list)
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

    def test_print_spielfeld_letzter_schuss(self):
        self.master.print_spielfeld(self.befuelltes_spielfeld_letzter_schuss)

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
        spielfeld:Spielfeld = self.master.platziere_schiff(Spielfeld(), Schiff("Schlachtschiff", 5), Koordinate("A",1, Richtung.SUEDEN))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_spielfeld(spielfeld)
            count_schiffe = fake_out.getvalue().count('#')
            self.assertEqual(count_schiffe, 5)

    def test_print_menu_correct_input(self):
        correct_input = "1"
        with patch('sys.stdin', new=StringIO(correct_input)):
            got_input:int = self.master.print_menu()
            self.assertEqual(int(correct_input), got_input)


    def test_print_countdown(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_countdown(2)
            count_anzeige:int = fake_out.getvalue().count("Anzeige")
            count_geloescht:int = fake_out.getvalue().count("geloescht.")
            count_2:int = fake_out.getvalue().count("2")
            count_1:int = fake_out.getvalue().count("1")
            self.assertEqual(count_anzeige, 2)
            self.assertEqual(count_geloescht, 2)
            self.assertEqual(count_2,1)
            self.assertEqual(count_1,1)

    def test_print_willkommensnachricht(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.master.print_willkommensnachricht()
            count_versenken:int = fake_out.getvalue().count("VERSENKEN")
            count_horizontal:int = fake_out.getvalue().count("═")
            count_vertical:int = fake_out.getvalue().count("║")
            count_new_lines:int = fake_out.getvalue().count("\n")
            self.assertEqual(count_versenken,1)    
            self.assertEqual(count_horizontal,142)
            self.assertEqual(count_vertical,16)  
            self.assertEqual(count_new_lines,10) 

    def test_get_user_input_richtung(self):
        correct_input = "1"
        expected_output = Richtung.OSTEN
        with patch('sys.stdin', new=StringIO(correct_input)):
            got_input:Richtung = self.master.get_user_input_richtung()
            self.assertEqual(expected_output, got_input)

    def test_get_user_input_name(self):
        with patch('sys.stdin', new=StringIO("Test1")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                got_input:Richtung = self.master.get_user_input_name(1)
                self.assertEqual(self.master.spieler_1.name, got_input)
                self.assertEqual(fake_out.getvalue(), "Name von Spieler 1: ")

    def test_fuehre_spielzug_aus(self):
        getroffen:bool = self.master.fuehre_spielzug_aus(self.test_koordinate_treffer)
        self.assertEqual(getroffen, True)
        daneben:bool = self.master.fuehre_spielzug_aus(self.test_koordinate_daneben)
        self.assertEqual(daneben, True)
        ungueltig:bool = self.master.fuehre_spielzug_aus(self.test_ungueltige_koordinate)
        self.assertEqual(ungueltig, False)

    @unittest.mock.patch('os.system')
    def test_clear_terminal(self, os_system:os):
        self.master.clear_terminal()
        if platform.system() == "Windows":
            os_system.assert_called_once_with('cls')
        elif platform.system() == "Linux":
             os_system.assert_called_once_with('clear')     
       
    def test_spielen_gueltige_koordinate(self):
        with patch('sys.stdin', new=StringIO("A1")):
            self.master.spielen()
            self.assertEqual(self.master.aktueller_spieler, self.spieler_2)

    def test_spielen_letzter_schuss(self):
        master = Master()
        spieler_1 = self.spieler_1
        master.aktueller_spieler = spieler_1
        spieler_2 = Spieler("Test2", self.befuelltes_spielfeld_letzter_schuss, Spielfeld(), 0)
        master.aktueller_gegner = spieler_2
        master.print_spielfeld(spieler_1.spielfeld)

        with patch('sys.stdin', new=StringIO("A1")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                master.spielen()
                self.assertEqual(master.ist_spiel_vorbei, True)
                ist_drin = False
                if "Glueckwunsch!" in fake_out.getvalue():
                    ist_drin = True
                self.assertEqual(ist_drin, True)

    def test_initialisieren(self):       
        with patch('sys.stdin', new=StringIO("tests\\test_speichern.json")):
            self.master.initialisieren(2)
            self.assertEqual(self.master.aktueller_spieler.name, "eins")
            self.assertEqual(self.master.aktueller_gegner.name, "zwei")

    def test_get_spieler_1(self):
        spieler = self.master.spieler_1
        self.assertEqual(self.spieler_1, self.master.spieler_1)

    def test_get_speichern_flag_bei_spielbeginn(self):
        expected_speicher_flag = False
        master = Master()
        speichern_flag = master.speichern_flag
        self.assertEqual(speichern_flag, expected_speicher_flag)

    def test_get_spieler_2(self):
        spieler = self.master.spieler_2
        self.assertEqual(self.spieler_2, self.master.spieler_2)


if __name__ == '__main__':
    unittest.main()
