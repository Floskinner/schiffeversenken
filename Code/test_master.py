from spieler import Spieler
import unittest
from spielfeld import Spielfeld
from koordinate import Koordinate
from schiff import Schiff
from master import Master
from helferklasse import Status


class Test_Master(unittest.TestCase):

    
    
    def setUp(self) -> None:
        self.master = Master()
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

        self.spieler_1 = Spieler("Test1", self.befuelltes_spielfeld, Spielfeld(),0)
        self.spieler_2 = Spieler("Test2", self.befuelltes_spielfeld, Spielfeld(), 0)
        self.test_koordinate_treffer = Koordinate('A',1)
        self.test_koordinate_daneben = Koordinate('E',1)
        return super().setUp()

    def test_print_spielfeld(self):       

        test_spielfeld = Spielfeld(spielfeld = self.befuelltes_spielfeld)
        self.master.print_spielfeld(test_spielfeld)

    def test_schiessen(self):
        self.master.schiessen(self.spieler_1, self.spieler_2)


if __name__ == '__main__':
    unittest.main()
