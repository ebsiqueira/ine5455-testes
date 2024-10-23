import unittest
import sys
import src.puzzle_game as puzzle_game
from io import StringIO

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)
   
    def test_coverage_get_tile_SCPath_1(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-3, 2)
 
    def test_coverage_get_tile_SCPath_2(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
            
    def test_coverage_get_tile_SCPath_3(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, " ")
        
    def test_coverage_get_tile_BCPath_1(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-3, 2)    
        
    def test_coverage_get_tile_BCPath_2(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(4, 2)  
        
    def test_coverage_get_tile_BCPath_3(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(3, -2)    
        
    def test_coverage_get_tile_BCPath_4(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(3, 5)    
        
    def test_coverage_get_tile_BCPath_5(self):
        tile = self.puzzle.get_tile(2, 3)
        self.assertEqual(tile, 6)   
        
    def test_coverage_get_tile_BCPath_6(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)   
        
    def test_coverage_get_tile_BCPath_7(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, " ") 
        
    # mutante 97: coloca lixo após print do numero    
    def test_mutante_97(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.puzzle.__print_board_of_puzzle_game__()
        sys.stdout = sys.__stdout__
        printed_value = captured_output.getvalue()
        
        self.assertEqual(printed_value, "1 2 3 \n4 5 6 \n7 8 - \n")
        
    # mutante 98: assume linha podendo ser 0    
    def test_mutante_98(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(0, 2)
            
    # mutante 99: assume linha a partir de 2, maior que 1
    def test_mutante_99(self):
        tile = self.puzzle.get_tile(1, 2)
        self.assertEqual(tile, 2)
        
    # mutante 101: coluna pode ser 0
    def test_mutante_101(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(2, 0)
      
    # mutante 102: coluna a partir de 2, maior que 1      
    def test_mutante_102(self):
        tile = self.puzzle.get_tile(2, 1)
        self.assertEqual(tile, 4)

if __name__ == '__main__':
    unittest.main()