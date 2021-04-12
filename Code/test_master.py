import unittest
from spielfeld import Spielfeld
from koordinate import Koordinate
from schiff import Schiff
from master import Master


class Test_Master(unittest.TestCase):

    def test_print_spielfeld(self):       
        befuelltes_spielfeld = [[2, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [2, 0, 1, 2, 0, 0, 0, 0, 0, 0],
                                [2, 0, 0, 0, 2, 2, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 2, 1, 2, 0, 0, 0, 2, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [-1, 0, 0, 0, 2, 2, 0, 0, 0, 0]]

        test_spielfeld = Spielfeld(spielfeld = befuelltes_spielfeld)
        
        master:Master = Master()
        master.print_spielfeld(test_spielfeld)


if __name__ == '__main__':
    unittest.main()
